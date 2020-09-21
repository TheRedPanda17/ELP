function checkCashRegister(price, cash, cid) {
    // Initialize objects
    let drawer = cid.map((moneyMap) => [...moneyMap]).reverse();
    let values = [100, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01];    
    let returnObj = { status: 'INSUFFICIENT_FUNDS', change: []};
    let due = cash - price;                                     
    let changeDue = {};                                         
  
    // Function to check total value of an array
    function getTotalDrawerMoney(arr) {
      let sum = 0;
      arr.map((slot) => {
        sum += slot[1];
      });
      return sum;
    }
  
    // Function to convert the number to their stupid standard (we should only used toFixed(2))
    function convertNumber(num) {
      if (!parseInt(num)){
        num = parseFloat(num.toFixed(2));
        if(num % 0.1 == 0)
          num = parseFloat(num.toFixed(1));
      }
      return num;
    }
  
    // Start with a simple check and return default object if success
    if(getTotalDrawerMoney(drawer) < due)
      return returnObj;
      
    // Iterate through each slot in drawer
    for(let i = 0; i < drawer.length; i++) {
      // Iterate while the due amount is larger than the coin/bill value and there is money in the slot
      while(due >= values[i] && drawer[i][1] != 0) {
        due -= values[i];                             
        drawer[i][1] -= values[i];                    
  
        // Add value in object if the field exists
        if (changeDue.hasOwnProperty(drawer[i][0])) 
          changeDue[drawer[i][0]] += values[i];
        // Set field and value in object if field does not exist
        else 
          changeDue[drawer[i][0]] = values[i];
  
        // Round the amount due because of tiny remainder problems
        due = due.toFixed(2);
      }
      // By this point, the slot will either be empty, or the amount due will be less than coin/bill amount
    }
  
    // Convert due object to desired array
    let changeDueArr = [];
    for(let property in changeDue){                 
      let num = convertNumber(changeDue[property]); 
      changeDueArr.push([property, num]);           
    }
  
    // If nothing is due and the amount of change is the same as the amount int the drawer
    if(due == 0 && getTotalDrawerMoney(changeDueArr) == getTotalDrawerMoney(cid))
      returnObj = { status: 'CLOSED', change: cid };        // Close regiester
    // If we have enough change
    else if(due == 0)
      returnObj = { status: 'OPEN', change: changeDueArr};   // Return change and keep register open
  
    // Not enough change
    return returnObj;
  }