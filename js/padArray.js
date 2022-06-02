// REMEMBER TO PSEUDOCODE
const pad = (array, minSize, value=null) => {
    let padding = array.length - minSize

    if (padding < 0){
        while(padding){
            array.push(value)
            padding += 1
        }
    }
    return array
}

console.log(pad([1,2,3], 5)) // should == [1,2,3,null,null]
console.log(pad([1,2,3], 5, 'apple')) // should == [1,2,3,'apple', 'apple']