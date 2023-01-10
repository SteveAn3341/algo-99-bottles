function bottleSong() {
  // code goes here
  let myBottles=99
  while(myBottles>2){
    console.log(`${myBottles} bottles of beer on the wall, ${myBottles} bottles of beer. Take one down and pass it around, ${myBottles-1} bottles of beer on the wall.`)
    myBottles--
  }
  console.log("2 bottles of beer on the wall, 2 bottles of beer. Take one down and pass it around, 1 bottle of beer on the wall.")
  console.log("1 bottles of beer on the wall, 1 bottles of beer. Take one down and pass it around, no more bottles of beer on the wall. No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall.")
};

bottleSong();
