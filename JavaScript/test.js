const list = [1, 2, 3, 4];

const cumulative = list.reduce((prev, next) => {
  return prev + next;
});
console.log(cumulative);
