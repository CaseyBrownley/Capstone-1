// // In script.js
// const jsonData = {
//             "name": "Luke Skywalker", 
//             "height": "172", 
//             "mass": "77", 
//             "hair_color": "blond", 
//             "skin_color": "fair", 
//             "eye_color": "blue", 
//             "birth_year": "19BBY", 
//             "gender": "male", 
//             "name": "C-3PO", 
//             "height": "167", 
//             "mass": "75", 
//             "hair_color": "n/a", 
//             "skin_color": "gold", 
//             "eye_color": "yellow", 
//             "birth_year": "112BBY", 
//             "gender": "n/a", 
//             "name": "R2-D2", 
//             "height": "96", 
//             "mass": "32", 
//             "hair_color": "n/a", 
//             "skin_color": "white, blue", 
//             "eye_color": "red", 
//             "birth_year": "33BBY", 
//             "gender": "n/a",
//   };

//   // In script.js
// const outputDiv = document.getElementById("output");

// // Option 1: Display as formatted JSON
// outputDiv.textContent = JSON.stringify(jsonData, null, 2);

// // Option 2: Display specific values
// outputDiv.innerHTML = `
//   <p>Name: ${jsonData.name}</p>
//   <p>Age: ${jsonData.age}</p>
//   <p>City: ${jsonData.city}</p>
// `;

// // Option 3: Display in a table
// const table = document.createElement("table");
// for (const key in jsonData) {
//   const row = table.insertRow();
//   const keyCell = row.insertCell();
//   const valueCell = row.insertCell();
//   keyCell.textContent = key;
//   valueCell.textContent = jsonData[key];
// }
// outputDiv.appendChild(table);