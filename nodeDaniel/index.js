import fs from 'fs';
import rdf from 'rdf-ext';
import ParserN3 from '@rdfjs/parser-n3';
import SHACLValidator from 'rdf-validate-shacl';
import { SolidNodeClient } from 'solid-node-client';
import $rdf from 'rdflib';
import {getSolidDataset} from '@inrupt/solid-client'
import mlspotlight from 'dbpedia-spotlight';




  // FUNTION FOR DBPEDIA SPOTLIGHT, WILL TEST TEXT FOR ANNOTATABLE DATA WHEN WORKING
  const input = "Detter er en test for om det er norsk";
  //const mlspotlight = mlspotlight();
  mlspotlight.annotate(input,function(output){
    console.log(output);
  })


async function loadFromPod(path) {
  const dataset = await getSolidDataset(path)
  return dataset
  // const stream = fs.createReadStream(path)
  // const parser = new ParserN3({ rdf })
  // return rdf.dataset().import(parser.import(stream))
}


const client = new SolidNodeClient();
await client.login({
  idp : "https://solidcommunity.net", // e.g. https://solidcommunity.net
  username : "mandalorian1337",
  password : "WT99im66wt",  
});



async function loadDataset (filePath) {
  const stream = fs.createReadStream(filePath)
  const parser = new ParserN3({ rdf })
  return rdf.dataset().import(parser.import(stream))
}

async function main() {

  // const path2 = 'https://mandalorian1337.solidcommunity.net/lexitags/bookmarks' //'https://martinclone.inrupt.net/public/test/dataset'
  // const path1 = 'https://martinclone.inrupt.net/public/test/shape'
  // const shapes = await loadFromPod(path1)
  // const data2 = await loadFromPod(path2)
  // const data = await loadDataset(data2)

  const shapes = await loadDataset('my-shapes2.ttl')
  const data = await loadDataset('my-data.ttl')

  const validator = new SHACLValidator(shapes, { rdf })
  const report = await validator.validate(data)

  // Check conformance: `true` or `false`
  console.log(report.conforms)

  for (const result of report.results) {
    // See https://www.w3.org/TR/shacl/#results-validation-result for details
    // about each property
    console.log(result.message)
    console.log(result.path)
    console.log(result.focusNode)
    console.log(result.severity)
    console.log(result.sourceConstraintComponent)
    console.log(result.sourceShape)
  }

  // Validation report as RDF dataset
  console.log(report.dataset)
}




main();