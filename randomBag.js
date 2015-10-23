var tetris = ["O", "I", "S", "Z", "L", "J", "T"];
var defTetris = ["O", "I", "S", "Z", "L", "J", "T"];

function tetrisPieces (count) {
  var ranOutput = [];
  while (ranOutput.length < count) {
    if (tetris.length > 0) {
      ranOutput += tetris.splice(Math.floor(Math.random() * tetris.length), 1);
    } else {
      tetris = defTetris.slice();
    }
  } return ranOutput;
}
