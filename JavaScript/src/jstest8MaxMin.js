var points = [40, 100, 1, 5, 25, 10, 432, 568, 344, 123, 334, 2365];
document.getElementById("demo").innerHTML = myArrayMax(points);

function myArrayMax(arr) {
  return Math.max.apply(null, arr);
}