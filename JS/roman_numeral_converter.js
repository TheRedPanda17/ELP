// Roman Numerals
function convertToRoman(num) {
    let numArr = [1000, 500, 100, 50, 10, 5, 1];
    let secondaryNums = [900, 400, 90, 40, 9, 4];
    let letterArr = ['M', 'D', 'C', 'L', 'X', 'V', 'I'];
    let secondaryLetters = ['CM', 'CD', 'XC', 'XL', 'IX', 'IV'];
    let romanString = '';

    while (num > 0) {
        for (let i = 0; i < numArr.length; i++) {
            if (num >= numArr[i]) {
                romanString += letterArr[i];
                num -= numArr[i];
                break;
            }
            else if (i < secondaryNums.length && num >= secondaryNums[i]) {
                romanString += secondaryLetters[i];
                num -= secondaryNums[i];
                break;
            }
        }
    }

    return romanString;
}