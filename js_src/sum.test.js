// index.test.js
//const sum = require('./sum').sum;
import { sum } from './sum';

test('adds 1 and 11 to get 12', () => {
    expect(sum(1, 11)).toBe(12);
});
