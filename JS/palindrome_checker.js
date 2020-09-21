function palindrome(str) {
    let arr = str
      .split('')
      .filter((letter) => /[^_\W]/.test(letter))
      .map((letter) => letter.toLowerCase());
  
    for (let i = 0; i < arr.length / 2; i++) 
      if (arr[i] != arr[arr.length - i - 1])
        return false;
    return true;
}