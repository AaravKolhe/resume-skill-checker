// Adapter only; OpenResume source is obtained separately.
const fs=require('fs'),path=require('path'),Module=require('module'),crypto=require('crypto');
const [pdfPath,checkout,dependencyDir,output,expectedFile]=process.argv.slice(2);
if(!expectedFile){console.error('Usage: node check_openresume.cjs PDF CHECKOUT DEPENDENCY_DIR OUTPUT_JSON EXPECTED_JSON');process.exit(2);}
if(fs.existsSync(output)){console.error('Refusing to overwrite audit');process.exit(2);}
const deps=Module.createRequire(path.resolve(dependencyDir,'package.json')),ts=deps('typescript');
const expected=JSON.parse(fs.readFileSync(expectedFile,'utf8'));
const before=crypto.createHash('sha256').update(fs.readFileSync(pdfPath)).digest('hex');
const root=path.resolve(checkout,'src/app'), out=path.resolve(output+'.modules');
function walk(dir){for(const e of fs.readdirSync(dir,{withFileTypes:true})){const p=path.join(dir,e.name);if(e.isDirectory())walk(p);else if(e.name.endsWith('.ts')&&!e.name.endsWith('.test.ts')){const dest=path.join(out,path.relative(root,p)).replace(/\.ts$/,'.js');fs.mkdirSync(path.dirname(dest),{recursive:true});fs.writeFileSync(dest,ts.transpileModule(fs.readFileSync(p,'utf8'),{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2020}}).outputText);}}}
walk(path.join(root,'lib/parse-resume-from-pdf'));
const orig=Module._resolveFilename;Module._resolveFilename=function(request,parent,...rest){if(request.startsWith('lib/'))request=path.join(out,request);return orig.call(this,request,parent,...rest);};
const pdfjs=deps('pdfjs-dist/build/pdf.js');
const {groupTextItemsIntoLines}=require(out+'/lib/parse-resume-from-pdf/group-text-items-into-lines');
const {groupLinesIntoSections}=require(out+'/lib/parse-resume-from-pdf/group-lines-into-sections');
(async()=>{const file=path.resolve(pdfPath);const pdf=await pdfjs.getDocument({data:new Uint8Array(fs.readFileSync(file)),fontExtraProperties:true}).promise;let items=[];for(let i=1;i<=pdf.numPages;i++){const page=await pdf.getPage(i);const content=await page.getTextContent();await page.getOperatorList();for(const item of content.items){const {str,dir,transform,fontName,...other}=item;items.push({...other,text:str.replace(/-­‐/g,'-'),x:transform[4],y:transform[5],fontName:page.commonObjs.get(fontName).name});}}
items=items.filter(x=>x.hasEOL||x.text.trim());const lines=groupTextItemsIntoLines(items),sections=groupLinesIntoSections(lines);let result={};for(const [file,fun] of [['extract-profile','extractProfile'],['extract-education','extractEducation'],['extract-work-experience','extractWorkExperience'],['extract-project','extractProject']])result[file]=require(out+'/lib/parse-resume-from-pdf/extract-resume-from-sections/'+file)[fun](sections);
const actual={profile:result['extract-profile'].profile,educations:result['extract-education'].educations,workExperiences:result['extract-work-experience'].workExperiences,projects:result['extract-project'].projects,sectionNames:Object.keys(sections)};
const findings=[];
function compare(want,got,at='resume'){
 if(Array.isArray(want)){if(!Array.isArray(got)||want.length!==got.length)findings.push({field:at,expectedCount:want.length,actualCount:got?.length});want.forEach((v,i)=>compare(v,got?.[i],at+'['+i+']'));}
 else if(want&&typeof want==='object'){for(const[k,v]of Object.entries(want))compare(v,got?.[k],at+'.'+k);}
 else if(typeof want==='string'){const norm=x=>String(x??'').normalize('NFKC').replace(/\s+/g,' ').trim();if(norm(want)!==norm(got))findings.push({field:at,expected:want,actual:got??null});}
 else if(want!==got)findings.push({field:at,expected:want,actual:got??null});
}
compare(expected,actual);
const after=crypto.createHash('sha256').update(fs.readFileSync(file)).digest('hex');if(before!==after)findings.push({field:'pdf',issue:'changed_during_check'});
const audit={status:findings.length?'issues_found':'checked',pdf:file,pdf_sha256:after,actual,findings,sections,limitations:'Local OpenResume grouping/profile/education/work/project functions with PDF.js adapter. Not deployed website. No dedicated Leadership/Honors field or full Skills extraction. Does not verify visual layout, factual truth or hiring eligibility.'};
fs.writeFileSync(output,JSON.stringify(audit,null,2));console.log(JSON.stringify({status:audit.status,findings},null,2));process.exitCode=findings.length?1:0;
})().catch(e=>{console.error(e.message);process.exitCode=2;});
