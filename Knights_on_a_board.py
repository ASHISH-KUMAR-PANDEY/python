horizontalCheck = (arr) => {
  let check = false;
   	for (let j = 0; j < arr.length; j++){
    let el = arr[j];
    	for(let i = 0; i < el.length; i++){
			let knight = el[i];
			let innerIndexRight = i + 2;
			let innerIndexLeft = i - 2;
			let outerIndex = j + 1;
			if(outerIndex > 7){
					break;
			}
        if(knight){
          if((arr[outerIndex][innerIndexRight]) || (arr[outerIndex][innerIndexLeft])){
            check = true;
          }
        }    
    }
  }
  return check;
}

verticalCheck = (arr) => {
    let check = false;
  for (let j = 0; j < arr.length; j++){
    let el = arr[j];
    for(let i = 0; i < el.length; i++){
        
        let knight = el[i];
        let innerIndexRight = i + 1;
        let innerIndexLeft = i - 1;
        let outerIndex = j + 2;
        if(outerIndex > 6){
            break;
        }
        
        if(knight){
          if((arr[outerIndex][innerIndexRight]) || (arr[outerIndex][innerIndexLeft])){
            
            check = true;
          }
        }    
    }
  }  
  return check;  
}

cannotCapture = (board) => {
	let cantCapture = true;
	let horizontal = horizontalCheck(board);
	let vertical = verticalCheck(board);
	if(horizontal || vertical){
		cantCapture = false;
	}
	return cantCapture;
}
