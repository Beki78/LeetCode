/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
    if (x < 0) {
      return false;
    }

   const str = x.toString()

   const reversed = str.split("").reverse().join("")

   return reversed == str
};

isPalindrome(121)
