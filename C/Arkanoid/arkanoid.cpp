#include <iostream>
#include <Util.h>
#include <conio.h>
#include <time.h>

#define boardW 60
#define boardH 25
#define barside 9
#define brickNum 1
#define lengthBrick 4

struct Pos2D {
    int x; int y;
    int ox; int oy;
};

Pos2D brick[60];

Pos2D obj;

int bar[barside];

int score, number, lives, speed;

bool endGame;

void drawBoard();

void menu();

int main(){	
	drawBoard();
    menu();
}

//SOUND

void nextLevelSound(){
	Beep(3500, 300);
	Beep(2500, 150);
	Beep(3000, 150);
	Beep(3500, 200);
	Beep(4000, 150);
	Beep(3000, 150);
	Beep(2000, 150);
	Beep(3500, 200);
}

void loseSound(){
	Beep(3500, 300);
	Beep(2500, 100);
	Beep(4000, 200);
	Beep(3500, 100);
	Beep(3000,  50);
	Beep(2500, 100);
	Beep(4000, 150);
	Beep(2000, 200);	
}

void gameOverSound(){ 
	Beep(4000, 400);
	Beep(3000, 300);
	Beep(2000, 300);
	Beep(3500, 400);
}

void winGameSound(){
	Beep(2000, 100);
	Beep(2200, 100);
	Beep(2400, 100);
	Beep(2600, 100);
	Beep(2800, 200);
	Sleep(200);
	Beep(4000, 100);	
	Sleep(1);
	Beep(4000, 100);	
	Sleep(1);
	Beep(4000, 100);	
	Sleep(1);
	Beep(4000, 100);
}
//SOUND

char level(int num){
	int i;
	switch(num)
	{
		case 1:
			brick[0].x = 22; brick[0].ox = 1; brick[0].y = 1;
			brick[1].x = 22; brick[1].ox = 1; brick[1].y = 2;
			brick[2].x = 22; brick[2].ox = 1; brick[2].y = 3;
			brick[3].x = 22; brick[3].ox = 1; brick[3].y = 4;
			brick[4].x = 22; brick[4].ox = 1; brick[4].y = 5;
			brick[5].x = 34; brick[5].ox = 1; brick[5].y = 1;
			brick[6].x = 34; brick[6].ox = 1; brick[6].y = 2;
			brick[7].x = 34; brick[7].ox = 1; brick[7].y = 3;
			brick[8].x = 34; brick[8].ox = 1; brick[8].y = 4;
			brick[9].x = 34; brick[9].ox = 1; brick[9].y = 5;
			brick[10].x = 26; brick[10].ox = 1; brick[10].y = 2;
			brick[11].x = 30; brick[11].ox = 1; brick[11].y = 3;

			break;
		case 2:
			brick[0].x = 12; brick[0].ox = 1; brick[0].y = 1;
			brick[1].x = 12; brick[1].ox = 1; brick[1].y = 2;
			brick[2].x = 12; brick[2].ox = 1; brick[2].y = 3;
			brick[3].x = 12; brick[3].ox = 1; brick[3].y = 4;
			brick[4].x = 12; brick[4].ox = 1; brick[4].y = 5;
			brick[5].x = 24; brick[5].ox = 1; brick[5].y = 1;
			brick[6].x = 24; brick[6].ox = 1; brick[6].y = 2;
			brick[7].x = 24; brick[7].ox = 1; brick[7].y = 3;
			brick[8].x = 24; brick[8].ox = 1; brick[8].y = 4;
			brick[9].x = 24; brick[9].ox = 1; brick[9].y = 5;
			brick[10].x = 16; brick[10].ox = 1; brick[10].y = 2;
			brick[11].x = 20; brick[11].ox = 1; brick[11].y = 3;

			brick[12].x = 32; brick[12].ox = 1; brick[12].y = 1;
			brick[13].x = 32; brick[13].ox = 1; brick[13].y = 2;
			brick[14].x = 32; brick[14].ox = 1; brick[14].y = 3;
			brick[15].x = 32; brick[15].ox = 1; brick[15].y = 4;
			brick[16].x = 32; brick[16].ox = 1; brick[16].y = 5;
			brick[17].x = 44; brick[17].ox = 1; brick[17].y = 1;
			brick[18].x = 44; brick[18].ox = 1; brick[18].y = 2;
			brick[19].x = 44; brick[19].ox = 1; brick[19].y = 3;
			brick[20].x = 44; brick[20].ox = 1; brick[20].y = 4;
			brick[21].x = 44; brick[21].ox = 1; brick[21].y = 5;
			brick[22].x = 36; brick[22].ox = 1; brick[22].y = 2;
			brick[23].x = 40; brick[23].ox = 1; brick[23].y = 3;

			break;
		case 3:
			brick[0].x = 3; brick[0].ox = 1; brick[0].y = 1;
			brick[1].x = 3; brick[1].ox = 1; brick[1].y = 2;
			brick[2].x = 3; brick[2].ox = 1; brick[2].y = 3;
			brick[3].x = 3; brick[3].ox = 1; brick[3].y = 4;
			brick[4].x = 3; brick[4].ox = 1; brick[4].y = 5;
			brick[5].x = 15; brick[5].ox = 1; brick[5].y = 1;
			brick[6].x = 15; brick[6].ox = 1; brick[6].y = 2;
			brick[7].x = 15; brick[7].ox = 1; brick[7].y = 3;
			brick[8].x = 15; brick[8].ox = 1; brick[8].y = 4;
			brick[9].x = 15; brick[9].ox = 1; brick[9].y = 5;
			brick[10].x = 7; brick[10].ox = 1; brick[10].y = 2;
			brick[11].x = 11; brick[11].ox = 1; brick[11].y = 3;

			brick[12].x = 22; brick[12].ox = 1; brick[12].y = 1;
			brick[13].x = 22; brick[13].ox = 1; brick[13].y = 2;
			brick[14].x = 22; brick[14].ox = 1; brick[14].y = 3;
			brick[15].x = 22; brick[15].ox = 1; brick[15].y = 4;
			brick[16].x = 22; brick[16].ox = 1; brick[16].y = 5;
			brick[17].x = 34; brick[17].ox = 1; brick[17].y = 1;
			brick[18].x = 34; brick[18].ox = 1; brick[18].y = 2;
			brick[19].x = 34; brick[19].ox = 1; brick[19].y = 3;
			brick[20].x = 34; brick[20].ox = 1; brick[20].y = 4;
			brick[21].x = 34; brick[21].ox = 1; brick[21].y = 5;
			brick[22].x = 26; brick[22].ox = 1; brick[22].y = 2;
			brick[23].x = 30; brick[23].ox = 1; brick[23].y = 3;

			brick[24].x = 41; brick[24].ox = 1; brick[24].y = 5;
			brick[25].x = 41; brick[25].ox = 1; brick[25].y = 4;
			brick[26].x = 41; brick[26].ox = 1; brick[26].y = 3;
			brick[27].x = 41; brick[27].ox = 1; brick[27].y = 2;
			brick[28].x = 45; brick[28].ox = 1; brick[28].y = 1;
			brick[29].x = 49; brick[29].ox = 1; brick[29].y = 1;
			brick[30].x = 53; brick[30].ox = 1; brick[30].y = 5;
			brick[31].x = 53; brick[31].ox = 1; brick[31].y = 4;
			brick[32].x = 53; brick[32].ox = 1; brick[32].y = 3;
			brick[33].x = 53; brick[33].ox = 1; brick[33].y = 2;
			brick[34].x = 49; brick[34].ox = 1; brick[34].y = 3;
			brick[35].x = 45; brick[35].ox = 1; brick[35].y = 3;
			
			break;
		default:
			break;
	}
}

void init(int cheatlive,int cheatlevel){
	int i;

 	score = 0, number = cheatlevel, lives = cheatlive;
	
	for (i = 0;i < 60; ++i){
		brick[i].y = 99;	
		brick[i].x = 99;
		brick[i].ox = 99;
	}
	
	speed = 100;
	
	level(number);

	endGame = false;
   	
 	for(i = 0;i < barside; ++i)
		bar[i]= i + 25;	
			
	obj.x = 29; obj.y =21;	
	obj.ox = 32; obj.oy =20;
}

void drawBoard(){
    ShowCur(false); // A^?n con tro?
	SetBGColor(14);
    for (int i = 0; i < boardW+1; i++) {
        for (int j = 0; j < boardH; j++) {
            	gotoxy(i, j);
				printf(" ");
    	}
    }
    SetBGColor(0);
    for (int i = 1; i < boardW ; i++) {
        for (int j = 1; j < boardH - 1; j++) {
            	gotoxy(i, j);
				printf(" ");
    	}
    }	
}

void clearBoard(){
    SetBGColor(0);
    for (int i = 1; i < 80 ; i++) {
        for (int j = 1; j < boardH - 1; j++) {
            if(i != boardW && i != boardW + 1){
				gotoxy(i, j);
				printf(" ");
            }
    	}
    }	
} 

void drawBrick(){
	SetColor(number);
	for (int i = 0;i < 60; ++i){
		if(brick[i].ox == 1){
			gotoxy(brick[i].x,brick[i].y);
			printf("%c%c%c%c",178,177,177,178);			
		}
		else if(brick[i].ox == 0){
			gotoxy(brick[i].x,brick[i].y);
			printf("    ");			
		}
	}
}

void drawObj(){
	SetColor(13);
//	printf("%d %d %d %d",obj.x,obj.ox,obj.oy,obj.y); getch();
	if (obj.x > 0 && obj.x < boardW  && obj.y > 0 && obj.y < boardH ){
		gotoxy(obj.x,obj.y);
		printf("%c",3);
	}
	if (obj.ox > 0 && obj.ox < boardW  && obj.oy > 0 && obj.oy < boardH )
		gotoxy(obj.ox,obj.oy);
		printf(" ");
}

void drawBar(){
	SetColor(7);
	for (int i = 0; i < barside; i++){
      	gotoxy(bar[i],22);
		printf("%c", 4); 
	}
}

void drawScore(){
	SetColor(15);
	gotoxy(64,5);
	printf("DIEM : %d",score);
}

void drawLives(){
	SetColor(15);
	gotoxy(64,8); printf("Lives");
	SetColor(13);
	gotoxy(64,9); for(int i = 0;i < lives;++i) printf("%c",3);
}

int checkEmpty(){
	for(int i = 0; i < 60; ++i)
		if (brick[i].ox == 1)
			return 0;
	return 1;
}

void checkLevel(){
	if (checkEmpty()){
		if(++number > 4){
			SetColor(9);
			gotoxy(19,12);printf("   You Win This Game   ");
			winGameSound(); Sleep(2000); clearBoard();
 			gotoxy(19,12); printf("This is a present 4 you");
			gotoxy(19,12); Sleep(2000); printf("           5           ");
			gotoxy(19,12); Sleep(1000); printf("           4           ");
			gotoxy(19,12); Sleep(1000); printf("           3           ");
			gotoxy(19,12); Sleep(1000); printf("           2           ");
			gotoxy(19,12); Sleep(1000); printf("           1           ");
			Sleep(1000);
			system("cls"); SetColor(15); system("present.exe"); exit(1);
			return;		
		}
		level(number);
	 	for(int i = 0;i < barside; ++i)
			bar[i]= i + 25;	
		obj.x = 29; obj.y =21;	
		obj.ox = 32; obj.oy =20;
		gotoxy(25,12); printf("Next Level"); Sleep(500); nextLevelSound(); Sleep(500);
		clearBoard();
	}
}

void checkOver(){
	if (lives < 0){
		SetColor(12); gotoxy(25,12); printf(" Game Over "); gameOverSound(); Sleep(1000);
	  	endGame = true;
  	}
  	if (obj.oy > 22) {  	
		level(number);
	 	for(int i = 0;i < barside; ++i)
			bar[i]= i + 25;	
  		speed = 100;
	  	obj.x = 29; obj.y =21;	
		obj.ox = 32; obj.oy =20;
  		lives--;
  		gotoxy(5,12); printf("       Mat 1 Mang Roi.Nhan SPACE De Tiep Tuc        ");
  		loseSound();
		while(1){
			if(_kbhit()) if(getch() == 32){
				gotoxy(5,12); printf("                                                    ");
				break;
			} 	
		}
		clearBoard();
  	}  	
}

void controlBar(){
	if (checkKey(KEY_LEFT) && bar[0] > 1) {
    	for(int i = 0;i < barside; ++i)
    		bar[i]=bar[i]-2; 
    		
 		gotoxy(bar[barside - 1]+1,22);
  		printf("  ");
	}
    else if (checkKey(KEY_RIGHT) && bar[barside - 1] < boardW - 1) {
    	for(int i = 0;i < barside; ++i)
    		bar[i]=bar[i]+2; 

    	gotoxy(bar[0]-2,22);
    	printf("  ");
  	}
}

void object(){
	// va cham vao brick
 	for(int i = 59; i >= 0; --i){
	  if (brick[i].ox == 1 && obj.y == brick[i].y && obj.x >= brick[i].x && obj.x < brick[i].x + 4)
	  {obj.oy = obj.y; obj.y += 1; brick[i].ox = 0;}
	  if (brick[i].ox == 1 && obj.x >= brick[i].x - 1 && obj.x <= brick[i].x + 4 && (obj.y == brick[i].y + 1 || obj.y == brick[i].y - 1) ){
			if (obj.x == brick[i].x - 1 && obj.y == brick[i].y + 1){
				if(obj.x == obj.ox + 3 && obj.y == obj.oy -1){
					obj.ox = obj.x; obj.oy = obj.y; 
	  				obj.x -= 3; obj.y += 1;
		  			brick[i].ox = 0;
			  		score += 100;
			  		printf("%c",07);
		  			return;	
  				}
			}
			else if (obj.x == brick[i].x - 1 && obj.y == brick[i].y - 1){
			  	if(obj.x == obj.ox + 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x -= 3; obj.y -= 1;  	
		  			brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;	
	  			}			
			}
			else if (obj.x == brick[i].x + 4 && obj.y == brick[i].y + 1){
  				if (obj.x == obj.ox - 3 && obj.y == obj.oy -1){
					obj.ox = obj.x; obj.oy = obj.y; 
				  	obj.x += 3; obj.y += 1;
		  			brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;	
  				}				
			}
			else if (obj.x == brick[i].x + 4 && obj.y == brick[i].y - 1){
	  			if(obj.x == obj.ox - 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x += 3; obj.y -= 1;  	
		  			brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;	
		  		}				}
			else if (obj.y == brick[i].y + 1){
				if(obj.x == obj.ox + 3 && obj.y == obj.oy -1){
					obj.ox = obj.x; obj.oy = obj.y; 
	  				obj.x += 3; obj.y += 1;
		  			brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;	
  				}
  				else if (obj.x == obj.ox - 3 && obj.y == obj.oy -1){
					obj.ox = obj.x; obj.oy = obj.y; 
				  	obj.x -= 3; obj.y += 1;
		  			brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;	
  				}
		  	}
  			else if (obj.y == brick[i].y - 1){
			  	if(obj.x == obj.ox + 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x += 3; obj.y -= 1;  	
		  			brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;	
	  			}
	  			else if(obj.x == obj.ox - 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x -= 3; obj.y -= 1;  	
		  			brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;	
		  		}
  			}
  		}
  		if (brick[i].ox == 1 && (obj.x == brick[i].x - 1 || obj.x == brick[i].x + 4) && obj.y == brick[i].y){
			if (obj.x == brick[i].x - 1){
				if (obj.x == obj.ox + 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x -= 3; obj.y += 1;  	
 					brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
			  		return;	
	  			}
  				else if(obj.x == obj.ox + 3 && obj.y == obj.oy -1){
					obj.ox = obj.x; obj.oy = obj.y; 
 					obj.x -= 3; obj.y -= 1;
 					brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
			  		return;
 				}
			}
			else if (obj.x == brick[i].x + 4){
				if(obj.x == obj.ox - 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x += 3; obj.y += 1;  	
	 				brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
			  		return;
	  			}
				else if (obj.x == obj.ox - 3 && obj.y == obj.oy -1){
					obj.ox = obj.x; obj.oy = obj.y; 
			  		obj.x += 3; obj.y -= 1;
		  			brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;	
			  	}
			}	 
		}
	}
 	for(int i = 59; i >= 0; --i){
  		if (brick[i].ox == 1 && (obj.x == brick[i].x - 2 && obj.x <= brick[i].x + 5) && (obj.y == brick[i].y + 1 || obj.y == brick[i].y - 1) ){
  			if(obj.x == brick[i].x - 2 && obj.y == brick[i].y + 1){
				if(obj.x == obj.ox + 3 && obj.y == obj.oy -1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x += 3; obj.y += 1;  	
	 				brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
				  	return;
			  	}
		  	}
  			else if(obj.x == brick[i].x - 5 && obj.y == brick[i].y - 1){
				if(obj.x == obj.ox - 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x -= 3; obj.y += 1;  	
	 				brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
			  		return;
	  			} 	
		  	}
  			else if(obj.x == brick[i].x - 2 && obj.y == brick[i].y - 1){
				if(obj.x == obj.ox + 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x += 3; obj.y -= 1;  	
	 				brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
			  		return;
	  			}  	
		  	}
  			else if(obj.x == brick[i].x + 5 && obj.y == brick[i].y - 1){
				if(obj.x == obj.ox - 3 && obj.y == obj.oy +1){
					obj.ox = obj.x; obj.oy = obj.y; 
					obj.x -= 3; obj.y += 1;  	
	 				brick[i].ox = 0;
			  		score += 100;
				  	printf("%c",07);
			  		return;
	  			}			  	
		  	}
  		}
 	}
 	  	
	// va cham vao bar

  	if (obj.x >= bar[0] - 1 && obj.x <= bar[barside - 1] + 1&& obj.y == 21){
		if(speed > 50) speed -= 2;	
	 	if(obj.x > bar[0] + 5){			
			obj.ox = obj.x; obj.oy = obj.y;  
			obj.x -= 3;	obj.y -= 1;
    	}
	  	else {
			obj.ox = obj.x; obj.oy = obj.y;  
	  		obj.x += 3; obj.y -= 1;	  		
	  	}
   	}

  	// va dap vao 3 canh theo chieu nguoc chieu kim dong ho

	else if (obj.x >= boardW - 1 && obj.ox == obj.x - 3 && obj.oy == obj.y +1){
		obj.ox = obj.x; obj.oy = obj.y;  
	  	obj.x -= 3; obj.y -= 1;
   	}
   	else if (obj.y <= 1 && obj.ox == obj.x + 3 && obj.oy == obj.y +1){
		obj.ox = obj.x; obj.oy = obj.y;  
	  	obj.x -= 3; obj.y += 1;
  	}
  	else if (obj.x <= 2 && obj.ox == obj.x + 3 && obj.oy == obj.y -1){
		obj.ox = obj.x; obj.oy = obj.y;  
	  	obj.x += 3; obj.y += 1;
 	}

  	// va dap vao 3 canh theo chieu kim dong ho

   	else if (obj.x >= boardW - 1 && obj.ox == obj.x - 3 && obj.oy == obj.y -1){
		obj.ox = obj.x; obj.oy = obj.y;  
	  	obj.x -= 3; obj.y += 1;
   	}
   	else if (obj.y <= 1 && obj.ox == obj.x - 3 && obj.oy == obj.y +1){
		obj.ox = obj.x; obj.oy = obj.y;  
	  	obj.x += 3; obj.y += 1;
  	}
  	else if (obj.x <= 2 && obj.ox == obj.x + 3 && obj.oy == obj.y +1){
		obj.ox = obj.x; obj.oy = obj.y;  
	  	obj.x += 3; obj.y -= 1;
 	}

   	// di chuyen theo chieu nguoc chieu kim dong ho
   	
  	else if(obj.ox == obj.x - 3 && obj.oy == obj.y +1){
		obj.ox = obj.x; obj.oy = obj.y;  
		obj.x += 3;	obj.y -= 1;
    }
	else if(obj.ox == obj.x + 3 && obj.oy == obj.y +1){
		obj.ox = obj.x; obj.oy = obj.y;  
	  	obj.x -= 3; obj.y -= 1;
  	}	
  	else if(obj.ox == obj.x + 3 && obj.oy == obj.y -1){
		obj.ox = obj.x; obj.oy = obj.y;  
	  	obj.x -= 3; obj.y += 1;
  	}
  	else if (obj.ox == obj.x - 3 && obj.oy == obj.y -1){
		obj.ox = obj.x; obj.oy = obj.y;  
		obj.x += 3; obj.y += 1;
  	}
	
}

void mainloop(){
	checkLevel();
	drawBrick();
	drawObj();
	controlBar();
	object();
	drawBar();
	drawScore();
	drawLives();
	checkOver();
}

void checkInit(){
	if(checkKey(KEY_H) && checkKey(KEY_A) && checkKey(KEY_C) && checkKey(KEY_O) && checkKey(KEY_Y) && checkKey(KEY_U) && checkKey(KEY_G) && checkKey(KEY_N)){
		clearBoard();
		int livecheat,levelcheat;
		while(_kbhit()) getch();
		do{
			gotoxy(5,12); printf("       Nhap Lives Em Muon Co (toi da 15 mang)       ");
			gotoxy(29,13); scanf("%d",&livecheat);
			if(livecheat > 15){
				clearBoard();
				gotoxy(5,12); printf("             Khong Duoc Dau Hehe :P                 ");
				Sleep(1000);
			}
		}while(livecheat > 15);
		clearBoard();
		do{
			gotoxy(5,12); printf("              Nhap Level Em Muon Choi               ");
			gotoxy(5,13); printf("        1,2,3 hay 4(4 la man xem hinh do hehe)      ");
			gotoxy(29,14); scanf("%d",&levelcheat);
			if(levelcheat > 4 || levelcheat < 1){
				clearBoard();
				gotoxy(5,12); printf("            Khong Co Man Nay Dau Hehe:P             ");
				Sleep(1000);
			}
		}while(levelcheat > 4 || levelcheat < 1);
		init(livecheat,levelcheat);
		return;
	}
	init(3,1);
}

void playGame(){
	mainloop();
	SetColor(15);
	gotoxy(5,12); printf("              Nhan SPACE de bat dau                 ");
	while(1){
		if(_kbhit()) if(getch() == 32){
			gotoxy(5,12); printf("                                                    ");
			break;
		} 	
	}
    while(!endGame){
		mainloop();
    	Sleep(speed);
    }
    menu();
}
void drawTextBar(int toadoY){
	gotoxy(21,toadoY); printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c",201,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,187);
	gotoxy(21,toadoY + 1); printf("%c",186); gotoxy(38,toadoY + 1); printf("%c",186);
	gotoxy(21,toadoY + 2); printf("%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c%c",200,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,205,188);
}

void instruction(){
	char a[20];
	clearBoard();
	gotoxy(5,5); printf("Em Yeu !");
	gotoxy(5,6); printf("Tro nay co 3 man, anh cho em 3 mang de choi, em vuot");
	gotoxy(5,7); printf("qua het thi se co dieu dac biet xay ra :P");
	gotoxy(5,12); printf("               Nhan ESC de tro lai                  ");
	while(1){
	if (_kbhit())
		if(getch()==27)	menu();	
	}
}

void showMenu(){
	gotoxy(26,3);
	SetColor(10);
	printf("ARKANOID");
	gotoxy(14,5);
	printf("Present For Nguyen Ngoc Anh (Em Yeu)");

	SetColor(3);
	drawTextBar(9);
	drawTextBar(12);
	drawTextBar(15);
	gotoxy(22,10); SetColor(12); printf("  Tro Choi Moi  ");
	gotoxy(22,13); SetColor(9) ; printf("    Huong Dan   ");
	gotoxy(22,16); SetColor(11); printf("      Thoat     ");

}
void menu(){
	clearBoard();
	showMenu();
	int toadoY = 9;
	SetColor(6);
	drawTextBar(toadoY);
	while(1){
		checkInit();
		if(checkKey(KEY_DOWN)){
			if(toadoY >= 9 && toadoY <= 12){
				toadoY += 3;
				showMenu();				
				SetColor(6);
				drawTextBar(toadoY);
			}
		}
		else if(checkKey(KEY_UP)){
			if(toadoY >= 12 && toadoY <= 15){
				toadoY -= 3;
				showMenu();				
				SetColor(6);
				drawTextBar(toadoY);				
			}
		}
		else if(checkKey(KEY_ENTER)){
			if(toadoY == 9){
				clearBoard();
				playGame();
				return;
			}
			else if(toadoY == 12) instruction();
			else if(toadoY == 15) exit(0);
		}
		Sleep(150);
	}
}
