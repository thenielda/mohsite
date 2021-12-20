
 var myRadios = document.getElementsByClassName('tab');
 var setCheck;
 var x = 0;
 for(x = 0; x < myRadios.length; x++){
     myRadios[x].onclick = function(){
         if(setCheck != this){
              setCheck = this;
         }else{
             this.checked = false;
             setCheck = null;
     }
     };
 }