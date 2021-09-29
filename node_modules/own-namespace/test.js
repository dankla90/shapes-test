const assert = require("assert");

//Test the non-rdflib functionality
const ns = require("./index.js")();
assert.equal(ns.schema("Recipe"), "http://schema.org/Recipe");

//Test the rdflib functionality
const rdflib = {
  namedNode: (val) => "RDF::" + val,
};
const rdfns = require("./index.js")(rdflib);
assert.equal(rdfns.schema("Recipe"), "RDF::http://schema.org/Recipe");

//Test custom namespace functionality
const customns = require("./index.js")(rdflib, './testns.json');
assert.equal(customns.example("Recipe"), "RDF::https://example.com/Recipe");

//Test custom namespace functionality with path from dotenv
const customDotns = require("./index.js")(rdflib);
assert.equal(customDotns.example("Recipe"), "RDF::https://example.com/Recipe");
