import { sum } from './sum';

const a = Number(document.getElementById('a').innerHTML); // get value of span with innerHTML
const b = Number(document.getElementById('b').innerHTML);

const c = sum(a, b);

const cElement = document.getElementById('c');

cElement.append(c);
