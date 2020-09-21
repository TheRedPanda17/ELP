function telephoneCheck(str) {
    let regEx = new RegExp(''
      + /^(1\s?)?/.source               // Optional 1 and spaces
      + /(\(\d{3}\)|\d{3})/.source      // Three numbers possibily surrounded by parenths
      + /[\s]*[-]?/.source              // Optional spaces and dashes
      + /\d{3}/.source                  // Three numbers
      + /[\s]*[-]?/.source              // Optional spaces and dashes
      + /\d{4}$/.source                 // Three numbers
    );
    return regEx.test(str);
}