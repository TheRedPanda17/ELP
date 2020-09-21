function rot13(str) {
    let arr = [];
    let letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
    arr = str
        .split('')
        .map((e) => {
            if (e.match(/[\W_]/i))
                return e;
            else {
                let index = letters.indexOf(e.toUpperCase());
                let indexCorrected = index >= 13 ? index - 13 : index + 13;
                return letters[indexCorrected];
            }
        });
    return arr.join('');
}