const array = [1, 2, 3, 4];

for (let i = 0; i < 4; i++) {
  array.push(array[i] * 2);
  console.log(array[i]);
}

console.log(array.length);
console.log(array[array.length - 1]);