document.write("<h1 class='elzero'>Elzero</h1>");
document.querySelector("h1.elzero").style.color = "blue" ;
document.querySelector("h1.elzero").style.textAlign = "center" ;
document.querySelector("h1.elzero").style.fontSize = "80px" ;
document.querySelector("h1.elzero").style.fontWeight = "bold" ;
document.querySelector("h1.elzero").style.fontFamily = "Arial" ;


console.log("%cElzero %cWeb %cSchool" ,
     "\
     color : red;\
     font-size : 40px;\
     " ,
      "\
      color : green;\
      font-weight : bold ; \
      font-size : 40px;\
      " ,
       "\
       color : white;\
       background-color : blue ;\
       font-size:40px;\
       ")


console.group("Group One")
console.log("Message One")
console.log("Message two")
console.group("Group two")
console.log("Message One")
console.log("Message two")
console.group("Group Three")
console.log("Message One")
console.log("Message two")
console.groupEnd()
console.groupEnd()
console.groupEnd()
console.group("Group Three")
console.log("Message One")
console.log("Message One")

console.table(["Elzero","Ahmed","Sameh","Gamal","Aya"])


// console.log("Iam In Console");
/* document.write("Iam In Page");*/
/* console.log("Iam In Console");
    document.write("Iam In Page");*/