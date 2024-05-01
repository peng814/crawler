// function add(a,b){
//     return a+b;
// }
//
// console.log(add(2,3))

const jsdom = require("jsdom");
const { JSDOM } = jsdom;

const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`);
const window = dom.window;

// 现在你可以使用 window 对象了
console.log(window.document.querySelector("p").textContent);
console.log(window.document)
