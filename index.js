/**
 * Need: 
 * 1. Clone Libmoji repo to local
 * 2. npm install libmoji
 * 
 */

const libmoji = require("libmoji");

let gender = libmoji.genders[libmoji.randInt(2)];
let style = libmoji.styles[libmoji.randInt(3)];
let traits = libmoji.randTraits(libmoji.getTraits(gender[0],style[0]));
let outfit = libmoji.randOutfit(libmoji.getOutfits(libmoji.randBrand(libmoji.getBrands(gender[0]))));

console.log(libmoji.buildPreviewUrl("fashion",3,gender[1],style[1],0,traits,outfit));