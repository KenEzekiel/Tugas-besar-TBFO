const date1 = Date("December 17, 1995 03:24:00");
// Sun Dec 17 1995 03:24:00 GMT...

const date2 = Date("1995-12-17T03:24:00");
// Sun Dec 17 1995 03:24:00 GMT...

const { bar, foo } = 1;
const { name } = obj;
const { age, id } = obj;
const email = obj.email;
const title = obj.title;
const colors = ["red"];
const [firstColor, secondColor] = colors;
const [first, ...rest] = colors;
const { a, ...rests } = { a: 1, b: 2, c: 3 };
// make an extreme math expression
let b = (((1 * 2 + 3 / 4 - (5 % 6 ** 7)) >>> 6) & 5) | (4 ^ 3);
