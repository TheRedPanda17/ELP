// Roman Numerals
function convertToRoman(num) {
    let numArr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    let letterArr = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'];
    let romanString = '';

    while (num > 0) {
        for (let i = 0; i < numArr.length; i++) {
            if (num >= numArr[i]) {
                romanString += letterArr[i];
                num -= numArr[i];
                break;
            }
        }
    }

    return romanString;
}