let score=JSON.parse(localStorage.getItem('score'));

         if(!score){
          score={
            wins:0,
            looses:0,
            ties:0
          };
                  }
         updateScore();
        
          function playGame(playerMove){
              if (playerMove === 'rock'){
                            if(computerMove === 'rock'){
                          result='tie';
                          }
                          else if(computerMove==='paper'){
                            result='you loose';
                          }
                          else if(computerMove==='scissors'){
                            result='you win';
                          }
              }else if(playerMove === 'paper'){
                          if(computerMove==='paper'){
                            result='tie';
                          }
                          else if(computerMove==='rock'){
                              result='you win';
                            }
                          else if(computerMove === 'scissors'){
                            result= 'you loose';
                            }
              }else if(playerMove === 'scissors'){
                            if(computerMove === 'scissors'){
                              result='tie';
                            }
                            else if(computerMove === 'rock'){
                            result= 'you loose';
                            }
                            else if(computerMove === 'paper'){
                                result= 'you win';
                            }
                           
                         }

                   if(result === 'you win'){
                     score.wins+=1;
                   }else if(result==='you loose'){
                     score.looses+=1;
                   } else if(result==='tie'){
                     score.ties+=1;
                   }  
                   
                   localStorage.setItem('score',JSON.stringify(score));
                  updateScore();
                  document.querySelector('.js-result').
                  innerHtml=result;
                 
                  
                  document.querySelector('.js-moves').
                  innerHTML=`You picked
                      <img src="${playerMove}-emoji.png" class="move-icon"><br>
                      computer picked
                      <img src="${computerMove}-emoji.png" class="move-icon">`;
                  
                  document.querySelector('.js-result').
                  innerHTML=`${result}`;
                       
                        } 
                        

                function updateScore(){
                  document.querySelector('.js-score')
                   .innerHTML=`wins:${score.wins} , looses:${score.looses}
                    , ties:${score.ties}`; 
                }


      let computerMove='';
     function pickComputerMove(){
              const randomNumber=Math.random();
              
              if(randomNumber>=0 && randomNumber<1/3){
                computerMove='rock';
              }
              else if(randomNumber>=1/3 && randomNumber<2/3){
                computerMove='paper';
              }
              else if(randomNumber >= 2/3 && randomNumber<1){
                computerMove='scissors';
              }
              console.log(computerMove);
   }