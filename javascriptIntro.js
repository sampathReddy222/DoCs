Dynamic Web Applications:
1. Client Server Communicaction
2. Manuplating HTML and CSS
3. Writing Application Logic
To develope Dynamic Web Applications there are two ways:
1. Using Java Script
2. Using Web Assembly
We use JS for user to interact with application more efficiently
Most of the Browsers understand JS
Most of the Developers Use Js
1. Go to inspect of any web page and navigate to console to write the Code. We can write js code in the Console.
Variables in JS:
C. let sam;
   sam = "sj";
Declaring and Assigning is Done above
console.log(sam) --- this will give the Value of the Declared Variable
if we do not assign any value to the Variable and try to use console.log() on the Variable, it will give undefined
DOM(Document Object Model):
----------Structural Representation of Content Present in the document Created by the Browser.
----------It allows the JS to Change Document Style, Content and Structure.
----------to Get Any Element of html use its id
----------document.getElementById("id")
----------to change the html element content use document.getElementById("id").textContent = "something"
----------to change the styling of any element use document.getElementById("id").style.property = "value"
----------to change an image of any element use document.getElementById("id").src = "image_url"
----------to perform action on any button use onclick Event <button onclick = "chang()">champ</button><script>function chang(){write your code here}</script>
----------this type of function creation is called function Decleration.
----------up on the clicking that button your code will execute and it will reflect on the UI based on the code.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
  Array : Array is a data structure
--- Data Structure will help us to store and organize data efficiently
--- They will allow us to eaisly access and perform Operations on the Data.
in JS we have Built in Data Structures like
1. Arrays
2. Objects
3. Maps
4. Sets
Array Holds ordered sequence of items.
------Creating Array:
------Ex:- let myArray = [2,"six",6.8]
------In arrays indexing Start from Zero Just like Python. Use indexes to access Elements of an Array ----Ex:- console.log(myArray[0])
------We can Even Modify elements in an Array using Index
------Ex:- myArray[1] = "Seven"
------     console.log(myArray[1])--- gives "Seven"
------To calculate no of items  in the Array we use Ex:- len = myArray.length
------Adding Elements in to the Array using push() method. By using this method we can add elements at the end of the Array.
------Ex:- myArray.push("give Element you want to add at the end of the Array")
------Removing Elements from an Array using pop(). This method will remove the Last element from the array and return its value.
------Ex:-  let arr = [1,2,34,]
            let lastEle = arr.pop()
			console.log(lastEle) --- gives 34
			console.log(arr) --- gives [1,2]
Creating an HTML element in JS
------To create we use -- let h1Element = document.createElement("h1") -- give the respective tags you want to create in place of "h1"
------Now to determine where this element should be present we use -- document.body.appendChild(h1Element) -- this element will be inside the body.
------To add elements created in JS to any of the Container elements.
------Get that respective element using id into a variable and append the element created in the JS using the Variable
------ Ex:- let divInHtmlDoc = document.getElementById("Element's_Id")
            divInHtmlDoc.appendChild(h1Element) ---- now the HTML h1 element will be inside that div Container.
Ceating a Function in JS using Function Expression:
------Syntax-------
let giveFunctionName = function(){
	write code in here.
}
giveFunctionName() -- call the function to Exicute the code inside the Function.
------To add classes of CSS in to JS for Styling we use:
------htmlElement.classList.add("give the class name here")
------To Remove Class we use:
------htmlElement.classList.remove("Write the  class name here")
------if we want somethign to happen after clicking on any HTML elements and to happen Dynamically use this type of function creation
------htmlElement.onclick = function(){
	  "write your code here" 
}
Object - it is another Data Stucture in JS
in JS we Have some Built in Data Structures:
1. Arrays
2. Objects
3. Maps
4. Sets
an Object is Collection of Properties (Key value pairs)
Creating an Object:
let person = {
	name:"sampath",
	age:25,
}
if we log this Person Object we get Object {name:"sampath",age:25}
Keys or Identifiers should no have spaces or should not start with Number
To use invalid Identifies give the Identifier in Quotes. ---- Ex:- let obj = {"Full name":"Sampath Reddy"}
Accessing property value of an object - there are two ways to access them 
1. dot Notation
2. bracket Notation
Ex:- console.log(person.name)--- gives sampath
     console.log(person["name"]) --- gives sampath
** use dot notation only when key is a valid Identifier.
** Bracket notation can be used for both valid and inValid Identifier.
** if try access any key which is not present in the Object we will get undefined -- Ex: - console.log(person["age"]) --- undefined
Ex:- let obj = {name:"sam"}
	 let a = "name"
	 console.log(obj[a]) --- gives sam --- here a will be considered as a variable
	 console.log(obj.a) --- gives undefined --- here a is considered as key , since we did not have any key with "name" it will return undefined
Object Destructuring:
To unpack properties from Object we use Object Destructuring
let obj = {name: "sam",age:25}
** The variable name should be same as the Key of the value we want to Destructure
let {name,age} = obj --- now console.log(name) --- gives name
Modifying Objects:
* We can use both dot and bracket notation:
Ex:- obj.name = "akl" or obj["name"] = "akl"
Adding new Property to the Object
* we can use both notations
Ex:- obj.gender = "male" or object["gender"] = "male"
Property values of an Object:
1. function
2. Array
3. Object.....many more
Ex: let obj = {name:"sam",add:function(){console.log("start adding")}
}
* Now to call that function which is in that object use ---- obj.add()
*** Ex: document.createElement() ----- here document is an object, createElement is a key and createElement() is a method.--- let document = {createElement:function(){"here we would have the  code that will help us to create HTML elemets in JS"}}
Assiging Arrays and Objects as values for a Object Properties
** Ex: let obj = {name:"sam",
fanLisa:["2",2],inobj:{class:"seven",student:"alive"}}
--------------------------------------------------------------------------------------------------------------------------------------------------------------
TODOS APPLICATION:
Input type "Check box"
In HTML:
<input type = "Checkbox" id = "myCheck"/>
** //we can give a label text for a checkbox input element which will refer to checkbox up on clicking that label text. for this we user <label> element
<label  for = "myCheck">checkbox</label> ** here id of the input element should be equal to "for" attribute value of the label element
//In JS:
let inputCheck = document.createElement("input")
inputCheck.type = "checkbox"
inputCheck.id = "myCheck"
let labelEl = document.createElement("label")
labelEl.htmlFor = "myCheck" or labelEl.setAttribute("for","myCheck")
labelEl.textContent = "Checked"
for setting attributes to html Elemnets in JS we  can use:
element.setAttribute(attributeName,attributeValue)
--------------------------------------------------
Static code of TODOS APPLICATION :
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous" />
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <script src="https://kit.fontawesome.com/5f59ca6ad3.js" crossorigin="anonymous"></script>
  </head>
  <body>
    <div class="todos-bg-container">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h1 class="todos-heading">Todos</h1>
            <h1 class="create-task-heading">
              Create <span class="create-task-heading-subpart">Task</span>
            </h1>
            <input type="text" id="todoUserInput" class="todo-user-input" />
            <button class="add-todo-button">Add</button>
            <h1 class="todo-items-heading">
              My <span class="todo-items-heading-subpart">Tasks</span>
            </h1>
            <ul class="todo-items-container" id="todoItemsContainer">
                <li class = "todo-item-container d-flex flex-row">
                    <input type = "checkbox" class = "checkbox-input" id = "myCheck"/>
                    <div class = "label-container d-flex flex-row">
                        <label for = "myCheck" class = "checkbox-label">Learn HTML</label>
                        <div class = "delete-icon-container">
                            <i class = "far fa-trash-alt delete-icon"></i>
                        </div>
                    </div>
                </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
---------------CSS--------------------------------------------------------------------------------------------------------------------------------------------
@import url("https://fonts.googleapis.com/css2?family=Bree+Serif&family=Caveat:wght@400;700&family=Lobster&family=Monoton&family=Open+Sans:ital,wght@0,400;0,700;1,400;1,700&family=Playfair+Display+SC:ital,wght@0,400;0,700;1,700&family=Playfair+Display:ital,wght@0,400;0,700;1,700&family=Roboto:ital,wght@0,400;0,700;1,400;1,700&family=Source+Sans+Pro:ital,wght@0,400;0,700;1,700&family=Work+Sans:ital,wght@0,400;0,700;1,700&display=swap");

.todos-bg-container {
  background-color: #f9fbfe;
  height: 100vh;
}
.todos-heading {
  text-align: center;
  font-family: "Roboto";
  font-size: 46px;
  font-weight: 500;
  margin-top: 20px;
  margin-bottom: 20px;
}
.create-task-heading {
  font-family: "Roboto";
  font-size: 32px;
  font-weight: 700;
}
.create-task-heading-subpart {
  font-family: "Roboto";
  font-size: 32px;
  font-weight: 500;
}
.todo-items-heading {
  font-family: "Roboto";
  font-size: 32px;
  font-weight: 700;
}
.todo-items-heading-subpart {
  font-family: "Roboto";
  font-size: 32px;
  font-weight: 500;
}
.todo-items-container {
  margin: 0px;
  padding: 0px;
}
.todo-item-container {
  margin-top: 15px;
}
.todo-user-input {
  background-color: white;
  width: 100%;
  border-style: solid;
  border-width: 1px;
  border-color: #e4e7eb;
  border-radius: 10px;
  margin-top: 10px;
  padding: 15px;
}
.add-todo-button {
  color: white;
  background-color: #4c63b6;
  font-family: "Roboto";
  font-size: 18px;
  border-width: 0px;
  border-radius: 4px;
  margin-top: 20px;
  margin-bottom: 50px;
  padding-top: 5px;
  padding-bottom: 5px;
  padding-right: 20px;
  padding-left: 20px;
}
.label-container {
  background-color: #e6f6ff;
  width: 100%;
  border-style: solid;
  border-width: 5px;
  border-color: #096f92;
  border-right: none;
  border-top: none;
  border-bottom: none;
  border-radius: 4px;
}
.checkbox-input {
  width: 20px;
  height: 20px;
  margin-top: 12px;
  margin-right: 12px;
}
.checkbox-label {
  font-family: "Roboto";
  font-size: 16px;
  font-weight: 400;
  width: 82%;
  margin: 0px;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-left: 20px;
  padding-right: 20px;
  border-radius: 5px;
}
.delete-icon-container {
  text-align: right;
  width: 18%;
}
.delete-icon {
  padding: 15px;
}
--------------------------------------------------------------------------------------------------------------------------------------------------------------
Creating TODOS APPLICATION in JS



 
