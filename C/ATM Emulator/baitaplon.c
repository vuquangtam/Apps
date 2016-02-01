/*
	Chuong Trinh Mo Phong ATM 
	Tai Khoan Co Dinh Dang Ten TK: 2221995xxxxx, VD: phan tu thu 1 222199500001.
	Vu Quang Tam.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <conio.h>
#include <time.h>
#include <windows.h>
#include <ctype.h>

#define MAX 10000	//so tk atm lon nhat co the luu duoc

typedef struct {
	char soTk[15];
	char pin[7];
	char tenTk[30];
	unsigned int soDu;
	char trangThai[60];
	char time[30];
	int active;    // active = 0 chua kich hoat, 2 la block, 1 la kich hoat
	char thongBao[60];
	int BoolThongbao; 
}khachHang;

void menu(char* );

int main(){
	char dir[30];
	menu(dir);
	return 0;
}


//=============================================================================================================

//CHUONG TRINH MO PHONG ATM

void gotoxy(int x, int y)
{
  static HANDLE h = NULL;  
  if(!h)
    h = GetStdHandle(STD_OUTPUT_HANDLE);
  COORD c = { x, y };  
  SetConsoleCursorPosition(h,c);
}

void numPad(){
	gotoxy(22,16);
	printf("ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»");
	gotoxy(22,17);
	printf("ºÚÄ ÚÄ ÚÄ     ÚÄÄÄÄÄÄº");
	gotoxy(22,18);
	printf("º³1 ³2 ³3     ³CLEAN º");
	gotoxy(22,19);
	printf("ºÚÄ ÚÄ ÚÄ     ÚÄÄÄÄÄÄº");
	gotoxy(22,20);
	printf("º³4 ³5 ³6     ³CANCELº");
	gotoxy(22,21);
	printf("ºÚÄ ÚÄ ÚÄ     ÚÄÄÄÄÄÄº");
	gotoxy(22,22);
	printf("º³7 ³8 ³9     ³ENTER º");	
	gotoxy(22,23);
	printf("º   ÚÄ               º");
	gotoxy(22,24);
	printf("º   ³0               º");
	gotoxy(22,25);
	printf("ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼");
}

void MenuPadShow(int choice){
	char ln1[60],ln2[60],ln3[60];
	switch(choice){
		case 0:
		strcpy(ln1,"                                                       ");
		strcpy(ln2,"                                                       ");
		strcpy(ln3,"                                                       ");
		break;
		case 1:
		strcpy(ln1,"ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		strcpy(ln2,"³                     INSERT ATM                      ³");
		strcpy(ln3,"ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		break;
		case 2:
		strcpy(ln1,"ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		strcpy(ln2,"³                 KIEM TRA TAI KHOAN                  ³");
		strcpy(ln3,"ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		break;
		case 3:
		strcpy(ln1,"ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		strcpy(ln2,"³                      RUT TIEN                       ³");
		strcpy(ln3,"ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		break;
		case 4:
		strcpy(ln1,"ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		strcpy(ln2,"³                    CHUYEN KHOAN                     ³");
		strcpy(ln3,"ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		break;
		case 5:
		strcpy(ln1,"ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		strcpy(ln2,"³                     DOI MA PIN                      ³");
		strcpy(ln3,"ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		break;
		case 6:
		strcpy(ln1,"ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		strcpy(ln2,"³                  SAO KE TAI KHOAN                   ³");
		strcpy(ln3,"ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		break;
		case 7:
		strcpy(ln1,"ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		strcpy(ln2,"³                      CONTINUE ?                     ³");
		strcpy(ln3,"ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		break;
	}
	gotoxy(0,0);
	printf("           ÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»     ");
	gotoxy(0,1);
	printf("           º²²NNA²BANK²²²²°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°º");
	gotoxy(0,2);
	printf("           ºÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛº");
	gotoxy(0,3);
	printf("           º%sº",ln1);
	gotoxy(0,4);
	printf("           º%sº",ln2);
	gotoxy(0,5);
	printf("           º%sº",ln3);
	gotoxy(0,6);
	printf("           º                                                       º");
	gotoxy(0,7);
	printf("           º                                                       º     ");
	gotoxy(0,8);
	printf("  ÚÄ       º                                                       º     ÚÄ");
	gotoxy(0,9);
	printf("  ³Q       º                                                       º     ³A");
	gotoxy(0,10);
	printf("  ÚÄ       º                                                       º     ÚÄ");
	gotoxy(0,11);
	printf("  ³W       º                                                       º     ³S");
	gotoxy(0,12);
	printf("  ÚÄ       º                                                       º     ÚÄ");
	gotoxy(0,13);
	printf("  ³E       º                                                       º     ³D");
	gotoxy(0,14);
	printf("           º                                                       º       ");
	gotoxy(0,15);
	printf("           ÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼");
	numPad();
}

int scanchar(){
	Nhap:
	fflush(stdin);
	switch(getch()){
		case 'q':
			gotoxy(2,8); printf("  ");
			gotoxy(2,9); printf(" ");
			Sleep(50);
			gotoxy(2,8); printf("ÚÄ");
			gotoxy(2,9); printf("³");
			return 113;
		case 'w':
			gotoxy(2,10); printf("  ");
			gotoxy(2,11); printf(" ");
			Sleep(50);
			gotoxy(2,10); printf("ÚÄ");
			gotoxy(2,11); printf("³");
			return 119;
		case 'e':
			gotoxy(2,12); printf("  ");
			gotoxy(2,13); printf(" ");
			Sleep(50);
			gotoxy(2,12); printf("ÚÄ");
			gotoxy(2,13); printf("³");
			return 101;		
		case 'a':
			gotoxy(73,8); printf("  ");
			gotoxy(73,9); printf(" ");
			Sleep(50);
			gotoxy(73,8); printf("ÚÄ");
			gotoxy(73,9); printf("³");
			return 97;
		case 's':
			gotoxy(73,10); printf("  ");
			gotoxy(73,11); printf(" ");
			Sleep(50);
			gotoxy(73,10); printf("ÚÄ");
			gotoxy(73,11); printf("³");
			return 115;
		case 'd':
			gotoxy(73,12); printf("  ");
			gotoxy(73,13); printf(" ");
			Sleep(50);
			gotoxy(73,12); printf("ÚÄ");
			gotoxy(73,13); printf("³");
			return 100;
		case '1':
			gotoxy(23,17); printf("  ");
			gotoxy(23,18); printf(" ");
			Sleep(50);
			gotoxy(23,17); printf("ÚÄ");
			gotoxy(23,18); printf("³");
			return 49;
		case '2':
			gotoxy(26,17); printf("  ");
			gotoxy(26,18); printf(" ");
			Sleep(50);
			gotoxy(26,17); printf("ÚÄ");
			gotoxy(26,18); printf("³");
			return 50;
		case '3':
			gotoxy(29,17); printf("  ");
			gotoxy(29,18); printf(" ");
			Sleep(50);
			gotoxy(29,17); printf("ÚÄ");
			gotoxy(29,18); printf("³");
			return 51;
		case '4':
			gotoxy(23,19); printf("  ");
			gotoxy(23,20); printf(" ");
			Sleep(50);
			gotoxy(23,19); printf("ÚÄ");
			gotoxy(23,20); printf("³");
			return 52;
		case '5':
			gotoxy(26,19); printf("  ");
			gotoxy(26,20); printf(" ");
			Sleep(50);
			gotoxy(26,19); printf("ÚÄ");
			gotoxy(26,20); printf("³");
			return 53;
		case '6':
			gotoxy(29,19); printf("  ");
			gotoxy(29,20); printf(" ");
			Sleep(50);
			gotoxy(29,19); printf("ÚÄ");
			gotoxy(29,20); printf("³");
			return 54;
		case '7':
			gotoxy(23,21); printf("  ");
			gotoxy(23,22); printf(" ");
			Sleep(50);
			gotoxy(23,21); printf("ÚÄ");
			gotoxy(23,22); printf("³");
			return 55;
		case '8':
			gotoxy(26,21); printf("  ");
			gotoxy(26,22); printf(" ");
			Sleep(50);
			gotoxy(26,21); printf("ÚÄ");
			gotoxy(26,22); printf("³");
			return 56;
		case '9':
			gotoxy(29,21); printf("  ");
			gotoxy(29,22); printf(" ");
			Sleep(50);
			gotoxy(29,21); printf("ÚÄ");
			gotoxy(29,22); printf("³");
			return 57;
		case '0':
			gotoxy(26,23); printf("  ");
			gotoxy(26,24); printf(" ");
			Sleep(50);
			gotoxy(26,23); printf("ÚÄ");
			gotoxy(26,24); printf("³");
			return 48;
		case 13:
			gotoxy(36,21); printf("       ");
			gotoxy(36,22); printf(" ");
			Sleep(50);
			gotoxy(36,21); printf("ÚÄÄÄÄÄÄ");
			gotoxy(36,22); printf("³");
			return 13;
		case 8:
			gotoxy(36,17); printf("       ");
			gotoxy(36,18); printf(" ");
			Sleep(50);
			gotoxy(36,17); printf("ÚÄÄÄÄÄÄ");
			gotoxy(36,18); printf("³");
			return 8;
		case 27:
			gotoxy(36,19); printf("       ");
			gotoxy(36,20); printf(" ");
			Sleep(50);
			gotoxy(36,19); printf("ÚÄÄÄÄÄÄ");
			gotoxy(36,20); printf("³");
			return 27;
		default:
			goto Nhap;
	}
}
int scannum(char s[],int size,int X,int Y){
	char ch=0;
	int i,x,y;
	Nhap:
	x=X,y=Y;
	for(i = 0;i < size;++i){
		gotoxy(X+i,Y);
		printf(" ");	
	}
	gotoxy(X,Y);
	memset(s,0,size);
	fflush(stdin);
	while (ch!=13){ //ch khác Enter
	fflush(stdin);
	ch=scanchar();
	if (ch==27) goto Nhap;
	if(ch>47 && ch<58){ //in cac ki tu so
	if ((strlen(s))<size-1){ //neu chuoi chua day
	gotoxy(x++,y);
	printf("%c",ch);;
	s[strlen(s)]=ch;
	}
	else gotoxy(X+size-1,Y);
	}
 	else	if (ch==8){ //backspace.
		if (s[0]){ //neu chuoi khac rong
			s[strlen(s)-1]=0; //xoa ki tu cuoi cung
			gotoxy(--x,y);
			printf(" %c",ch); // |   xoa ki tu truoc do tren man hinh
		}
		else gotoxy(X,Y);
		}
	}
	printf("\n");
	fflush(stdin);
}

void scanpin(char s[],int size,int X,int Y){ // chuong trinh mat khau dau *
	char ch=0;
	int i,x,y;
	Nhap:
	x=X,y=Y;
	for(i = 0;i < size;++i){
		gotoxy(X+i,Y);
		printf(" ");	
	}
	gotoxy(X,Y);
	memset(s,0,size);
	fflush(stdin);
	while (ch!=13){ //ch khác Enter
	fflush(stdin);
	ch=scanchar();
	if (ch==27) goto Nhap;	
	if (ch<=0)
		getch(); // loai bo cac ki tu dieu khien
	else if(ch>47 && ch<58){ //in cac ki tu so
	if ((strlen(s))<size-1){ //neu chuoi chua day
	gotoxy(x++,y);
	printf("*");;
	s[strlen(s)]=ch;
	}
	else gotoxy(X+size-1,Y);
	}
		else if (ch==8){ //backspace.
		if (s[0]){ //neu chuoi khac rong
			s[strlen(s)-1]=0; //xoa ki tu cuoi cung
			gotoxy(--x,y);
			printf(" %c",ch);
		}
		else gotoxy(X,Y);	
		}
	}
	printf("\n");
	fflush(stdin);
}


int readnum(char* dir,int choice){ //ham xuat ra so tiep theo tu CSDL , dir la ten CSDL (nameATM.txt,soTk.txt)
	FILE *fp;
	fp = fopen(dir,"r+");
	if (fp == NULL){ // neu nhu chua khoi tao thi khoi tao. gan gia tri dau tien bang 1
		int result = 1;
		fp = fopen(dir,"w");
		if (choice == 1){
			fprintf(fp,"\n%d",result);
		}
		fclose(fp);
		return result;
	}
	else{
		int i=0,result;
		char temp,number[20];
		fseek(fp,0,2);
		while((temp=fgetc(fp))!='\n'){ //kiem tra vi tri cua so cuoi cung
			fseek(fp,-2,1);
		}
		while(!feof(fp)){
			number[i++]=fgetc(fp); //quet so vao mang number
		}
		result = atoi(number) + 1;
		if (choice == 1){
			fprintf(fp,"\n%d",result);
		} // in gia tri ke tiep vao CSDL
		fclose(fp);
		return result;
	}
}

void MenuWelcome(){
	MenuPadShow(0);
	gotoxy(12,1);
	printf("²²NNA²BANK²²²²°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,2);                                                         
	printf("ÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛ");
	gotoxy(12,3);
	printf("                                                       ");
	gotoxy(12,4);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,5);
	printf("                                                       ");
	gotoxy(12,6);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,7);
	printf("                                                       ");
	gotoxy(12,8);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,9);
	printf("                                                       ");
	gotoxy(12,10);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,11);
	printf("                                                       ");
	gotoxy(12,12);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,13);
	printf("                                                       ");
	gotoxy(12,14);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,7);
	Sleep(400);
	printf("°°°°°.-. .-. .-. .-.   .-. .-. . . .-. . . .-. .-.°°°°°");
	gotoxy(12,8);
	Sleep(400);
	printf("°°°°°|-  |-| `-.  |    |-| |  )| | |-| | | |   |- °°°°°");
	gotoxy(12,9);
	Sleep(400);
	printf("°°°°°'   ` ' `-'  '    ` ' `-' `.' ` ' ' ` `-' `-'°°°°°");
	Sleep(3000);
}

int MenuLanguage(){
	char ch;
	MenuPadShow(0);
	gotoxy(12,3);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,4);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,5);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,6);
	printf("°°°°°°°°°°°°°°°°°SELECT YOUR LANGUAGE°°°°°°°°°°°°°°°°°°");
	gotoxy(12,7);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,8);
	printf("°°°°°°°°°°°°°°°°°°°°CHON NGON NGU°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,9);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,10);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,11);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,12);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,13);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,14);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(14,8);
	printf("ÉÍÍÍÍÍÍÍÍÍÍÍÍ»");
	gotoxy(14,9);
	printf("º TIENG VIET º");
	gotoxy(14,10);
	printf("ÈÍÍÍÍÍÍÍÍÍÍÍÍ¼");
	gotoxy(51,8);
	printf("ÉÍÍÍÍÍÍÍÍÍÍÍÍ»");
	gotoxy(51,9);
	printf("º  ENGLISH   º");
	gotoxy(51,10);
	printf("ÈÍÍÍÍÍÍÍÍÍÍÍÍ¼");
	while(1){
		fflush(stdin);
		ch = scanchar();
		if(ch == 'q'){
			return 1;
		}
		else if(ch == 'a'){
			return 0;
		}
	}
}

void MenuGoodbye(){
	MenuPadShow(0);
	gotoxy(12,1);
	printf("²²NNA²BANK²²²²°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,2);                                                         
	printf("ÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛ");
	gotoxy(12,3);
	printf("                                                       ");
	gotoxy(12,4);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,5);
	printf("                                                       ");
	gotoxy(12,6);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,7);
	printf("                                                       ");
	gotoxy(12,8);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,9);
	printf("                                                       ");
	gotoxy(12,10);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,11);
	printf("                                                       ");
	gotoxy(12,12);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,13);
	printf("                                                       ");
	gotoxy(12,14);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,7);
	Sleep(400);
	printf("°°°  ___   __    __  ____    ____  _  _  ____    _  °°°");
	gotoxy(12,8);
	Sleep(400);
	printf("°°° / __) /  \\  /  \\(    \\  (  _ \\( \\/ )(  __)  / \\ °°");
	gotoxy(12,9);
	Sleep(400);
	printf("°°°( (_ \\(  O )(  O )) D (   ) _ ( )  /  ) _)   \\_/ °°°");
	gotoxy(12,10);
	Sleep(400);
	printf("°°° \\___/ \\__/  \\__/(____/  (____/(__/  (____)  (_) °°°");
	Sleep(1000);
}

void Notification(){
	MenuPadShow(0);
	gotoxy(12,1);
	printf("²²NNA²BANK²²²²°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,2);                                                         
	printf("ÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛÛ");
	gotoxy(12,3);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,4);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,5);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,6);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,7);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,8);
	printf(" ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ");
	gotoxy(12,9);
	printf("° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °");
	gotoxy(12,10);
	printf(" ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ");
	gotoxy(12,11);
	printf("° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °");
	gotoxy(12,12);
	printf(" ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ");
	gotoxy(12,13);
	printf("° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° ° °");
	gotoxy(12,14);
	printf("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°");
	gotoxy(12,6);
	printf("     Ban Co Thong Bao Moi. Nhan Phim Bat Ky De Xem     ");
	scanchar();
	gotoxy(12,6);
	printf("                                                       ");
	Sleep(100);			
}

void getpin(char s[], int size){ // chuong trinh mat khau dau *
	char ch=0;
	memset(s,0,size);
	fflush(stdin);
	while (ch!=13){ //ch khác Enter
	fflush(stdin);
	ch=getch();
	if (ch<=0)
		getch(); // loai bo cac ki tu dieu khien
	else if(ch>47 && ch<58){ //in cac ki tu so
	if ((strlen(s))<size-1){ //neu chuoi chua day
	printf("*");;
	s[strlen(s)]=ch;
	}
	}
		else if (ch==8){ //backspace.
		if (s[0]){ //neu chuoi khac rong
			s[strlen(s)-1]=0; //xoa ki tu cuoi cung
			printf("%c ",ch); // |   xoa ki tu truoc do tren man hinh
			printf("%c",ch); //  |
		}
		}
	}
	printf("\n");
	fflush(stdin);
}

char* makeDir(char* dir,int num){ //ham tao duong dan tu so lieu lay tu CSDL
	char temp[20],*dirLog;
	itoa(num,temp,10);				// noi string thanh dang acc[%d].dat.
	strcpy(dir,"acc");      		//
	strcat(dir,temp);				//
	strcat(dir,".dat");				//
}

void makesoTk(char* soTk,int num){	//tao so tai khoan voi dinh dang 2221995xxxxx
	char temp[7];
	strcpy(soTk,"2221995");				//tao so tai khoan
	itoa(MAX+num,temp,10);
	strcat(soTk,temp);
}

char* getTime(){	// ham lay thong tin thoi gian hien tai
	time_t now = time(0);
	return asctime(localtime(&now));
}

void printInfo(khachHang khach, int choice,char* trangThai){
/*
	 ham in thong tin , neu choice = 1 thi in ra password
	 choice = 1 ( createAcc ), 2 (EditAcc), 3 (con lai)
*/	
		printf(" |   So Tai Khoan            : %s\n",khach.soTk);
		printf(" |   Ten Tai Khoan           : %s\n",khach.tenTk);
		if (choice == 1 || choice == 2){
		printf(" |   Ma PIN                  : %s\n",khach.pin);
		}
		printf(" |   So Du                   : %d VND\n",khach.soDu);
		printf(" |   Trang Thai              : %s\n",trangThai);
		if (choice == 1){
			printf(" |   Thoi Gian Tao Tai Khoan : %s\n",khach.time);
		}
		else{
			printf(" |   Thoi Gian               : %s\n",khach.time);
		}
	}

int	yesNo(){	// Chuong Trinh Kiem Tra YES NO, Neu Nhap y hoac Y thi tra ve 1, n hoac N
	char check;	// thi tra ve 0, nhap khac thi nhap lai
	while(1){
	check = getch();
	if(check == 'y' || check == 'Y')
	return 1;
	else if(check == 'n' || check == 'N')
	return 0;
	}
}

int yesNoAnimation(){
	gotoxy(60,10);
	printf("ÚÄÄÄÄÄ¿");
	gotoxy(60,11);
	printf("³ YES ³");
	gotoxy(60,12);
	printf("%cÄÄÄÄÄ´",195);
	gotoxy(60,13);
	printf("³ NO  ³");
	gotoxy(60,14);
	printf("ÀÄÄÄÄÄÙ");
	char check;
	while(1){
	fflush(stdin);
	check = scanchar();
	if(check == 's')
	return 1;
	else if(check == 'd')
	return 0;
	}	
}

void GraphAnimation(x,y){		// muc dich : de cho dau '.' chay theo 500ms ( dep mat )
	gotoxy(x++,y);Sleep(500);
	printf(".");
	gotoxy(x++,y);Sleep(500);
	printf(".");
	gotoxy(x++,y);Sleep(500);
	printf(".");
	gotoxy(x++,y);Sleep(500);
	printf(".");
	Sleep(500);
}

void animation(){		// muc dich : de cho dau '.' chay theo 500ms ( dep mat )
	Sleep(500);
	printf(".");
	Sleep(500);
	printf(".");
	Sleep(500);
	printf(".");
	Sleep(500);
	printf(".");
	Sleep(500);
}
void insertATManimation(){
	gotoxy(54,16); printf("ÉÍÍÍÍÍÍÍÍÍÍÍ»");
	gotoxy(54,17); printf("º³Û³³Û³Û³³³Ûº");
	gotoxy(54,18); printf("ÈÍÍÍÍÍÍÍÍÍÍÍ¼");
	Sleep(200);
	gotoxy(54,16); printf("º³Û³³Û³Û³³³Ûº");
	gotoxy(54,17); printf("ÈÍÍÍÍÍÍÍÍÍÍÍ¼");
	gotoxy(54,18); printf("             "); 
	Sleep(200);
	gotoxy(54,16); printf("ÈÍÍÍÍÍÍÍÍÍÍÍ¼");
	gotoxy(54,17); printf("             ");
	gotoxy(54,18); printf("             "); 
	Sleep(200);
	gotoxy(54,16); printf("             ");
	gotoxy(54,17); printf("             ");
	gotoxy(54,18); printf("             "); 
	
}

void pushATManimation(){
	gotoxy(54,16); printf("             ");
	gotoxy(54,17); printf("             ");
	gotoxy(54,18); printf("             "); 
	Sleep(200);
	gotoxy(54,16); printf("ÈÍÍÍÍÍÍÍÍÍÍÍ¼");
	gotoxy(54,17); printf("             ");
	gotoxy(54,18); printf("             "); 
	Sleep(200);
	gotoxy(54,16); printf("º³Û³³Û³Û³³³Ûº");
	gotoxy(54,17); printf("ÈÍÍÍÍÍÍÍÍÍÍÍ¼");
	gotoxy(54,18); printf("             "); 
	Sleep(200);
	gotoxy(54,16); printf("ÉÍÍÍÍÍÍÍÍÍÍÍ»");
	gotoxy(54,17); printf("º³Û³³Û³Û³³³Ûº");
	gotoxy(54,18); printf("ÈÍÍÍÍÍÍÍÍÍÍÍ¼");
	Sleep(200);
	gotoxy(54,16); printf("             ");
	gotoxy(54,17); printf("ÉÍÍÍÍÍÍÍÍÍÍÍ»");
	gotoxy(54,18); printf("º³Û³³Û³Û³³³Ûº");
	gotoxy(54,19); printf("ÈÍÍÍÍÍÍÍÍÍÍÍ¼");
	Sleep(200);
	gotoxy(54,16); printf("             ");
	gotoxy(54,17); printf("             ");
	gotoxy(54,18); printf("ÉÍÍÍÍÍÍÍÍÍÍÍ»");
	gotoxy(54,19); printf("º³Û³³Û³Û³³³Ûº");
	gotoxy(54,20); printf("ÈÍÍÍÍÍÍÍÍÍÍÍ¼");
	Sleep(200);
	gotoxy(54,18); printf("             ");
	gotoxy(54,19); printf("             ");
	gotoxy(54,20); printf("             "); 
	
}

void printLog(char *dir,khachHang temp){
	// in vao file log
	FILE *fp;
	char dirLog[30];
	strcpy(dirLog,dir);
	dirLog[strlen(dirLog) - 4] = NULL;
	strcat(dirLog,"_log.dat");
	fp = fopen(dirLog,"a+b");
	fwrite(&temp,sizeof(temp),1,fp);
	fclose(fp);
	// in vao file log
}

void printUserLog(char *dir,khachHang temp){
	// in vao file user log
	FILE *fp;
	char dirLog[30];
	strcpy(dirLog,dir);
	dirLog[strlen(dirLog) - 4] = NULL;
	strcat(dirLog,"_log_user.dat");
	fp = fopen(dirLog,"a+b");
	fwrite(&temp,sizeof(temp),1,fp);
	fclose(fp);
	// in vao file user log
}

int logReader(){	
	int num;
	FILE *fp;
	char dir[30];
	khachHang temp;
	Nhap:
	system("cls");
	printf("\n====================Xem File Log=====================\n");
	printf("\n #Nhap Ma So The : ");
	scanf("%d",&num);
	makeDir(dir,num);
	dir[strlen(dir) - 4] = NULL;
	strcat(dir,"_log.dat");
	if((fp=fopen(dir,"rb")) == NULL){
		fclose(fp);
		int choice;
		do{
			printf("\n Account Nay Chua Co File Log. Ban Muon\n");
			printf("\n ---1.Nhap Ma So The Khac\n");
			printf("\n ---2.Tro Ve Menu\n");
			printf("\n #Chon : ");
			fflush(stdin); scanf("%d",&choice);
			switch (choice){
				case 1 :
					system("cls");
					goto Nhap;
					break;
				case 2 :
					return 0;
				default :
				system("cls");
				printf("\n====================Xem File Log=====================\n");
				printf("\n #Nhap Ma So The : %d\n",num);
				break;
			}
		}while(choice > 2 || choice < 1 );
	}
	else{
		printf("\n\n\n\n");
		while(fread(&temp,sizeof(temp),1,fp) == 1){
			printInfo(temp,2,temp.trangThai);
			printf("\n\n");
		}
		printf("\n Nhan Phim Bat Ky De Quay Ve Menu\n");
		getch();
		return 1;
	}
}


void inPhieu(char *dir,char* trangThai,int tittle){	// Chuong trinh in phieu nhay theo tung 500 ms
	FILE *fp;
	khachHang khach;
	fp = fopen(dir,"rb");
	fread(&khach,sizeof(khach),1,fp);
	fclose(fp);
	MenuPadShow(tittle);
	gotoxy(12,9);
	printf("                 Ban Co Muon In Phieu                  ");
	if (yesNoAnimation() == 1){
		gotoxy(12,9);
		printf("                                                       ");
		khach.time[strlen(khach.time)-1] = ' ';
		gotoxy(12,7);
		printf("           ...Dang In.....................             ");
		gotoxy(12,26);
		Sleep(500);
		printf("ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		gotoxy(12,27);
		Sleep(500);
		printf("³                      PHIEU                           ³");
		gotoxy(12,28);
		Sleep(500);
		printf("³                                                      ³");
		gotoxy(12,29);
		Sleep(500);
		printf("³ So Tai Khoan  : %-37s³",khach.soTk);
		gotoxy(12,30);
		Sleep(500);
		printf("³ Ten Tai Khoan : %-37s³",khach.tenTk);
		gotoxy(12,31);
		Sleep(500);
		printf("³ So Du         : %-37d³",khach.soDu);
		gotoxy(12,32);
		Sleep(500);
		printf("³ Trang Thai    : %-37s³",trangThai);
		gotoxy(12,33);
		Sleep(500);
		printf("³ Thoi Gian     : %-37s³",khach.time);
		gotoxy(12,34);
		Sleep(500);
		printf("ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		gotoxy(12,9);
		printf("           ...Xong........................             ");
		scanchar();
		gotoxy(12,26);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,27);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,28);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,29);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,30);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,31);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,32);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,33);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,34);
		Sleep(50);
		printf("                                                        ");
		}
	else return;
}

void NhanTien(unsigned int tien){	
	MenuPadShow(3);
		gotoxy(12,7);
		printf("           ...............................             ");
		gotoxy(12,26);
		Sleep(500);
		printf("ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
		gotoxy(12,27);
		Sleep(500);
		printf("³           CONG HOA XA HOI CHU NGHIA VIET NAM         ³");
		gotoxy(12,28);
		Sleep(500);
		printf("³                                                      ³");
		gotoxy(12,29);
		Sleep(500);
		printf("³                %12d VND                      ³",tien);
		gotoxy(12,30);
		Sleep(500);
		printf("³                                                      ³");
		gotoxy(12,31);
		Sleep(500);
		printf("³                                         BI 088645997 ³");
		gotoxy(12,32);
		Sleep(500);
		printf("ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ");
		gotoxy(12,9);
		printf("           ...Xong........................             ");
		scanchar();
		gotoxy(12,26);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,27);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,28);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,29);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,30);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,31);
		Sleep(50);
		printf("                                                        ");
		gotoxy(12,32);
		Sleep(50);
		printf("                                                        ");
}

int MenuTien(){
	gotoxy(12,8);
	printf(" ÚÄÄÄÄÄÄÄÄÄÄÄ¿                           ÚÄÄÄÄÄÄÄÄÄÄÄ¿ ");
	gotoxy(12,9);
	printf(" ³   50000   ³                           ³   500000  ³ ");
	gotoxy(12,10);
	printf(" %cÄÄÄÄÄÄÄÄÄÄÄ´                           %cÄÄÄÄÄÄÄÄÄÄÄ´ ",195,195);
	gotoxy(12,11);
	printf(" ³  100000   ³                           ³  1000000  ³ ");
	gotoxy(12,12);
	printf(" %cÄÄÄÄÄÄÄÄÄÄÄ´                           %cÄÄÄÄÄÄÄÄÄÄÄ´ ",195,195);
	gotoxy(12,13);
	printf(" ³  200000   ³                           ³  So Khac  ³ ");
	gotoxy(12,14);
	printf(" ÀÄÄÄÄÄÄÄÄÄÄÄÙ                           ÀÄÄÄÄÄÄÄÄÄÄÄÙ ");
	Nhap:
	switch(scanchar()){
		case 'q':
			return 50000;
		case 'w':
			return 100000;
		case 'e':
			return 200000;
		case 'a':
			return 500000;
		case 's':
			return 1000000;
		case 'd':
			return 0;
		case 27 :
			return 1;
		default :
			goto Nhap;
	}
}

int insertATM(char *dir){    // ham nhap the ATM
	FILE *fp;
	int num,choice;
	khachHang khach;
	char tempnum[6];
	Nhap:
	MenuPadShow(1);
	gotoxy(12,6);
	printf("          ------------Dua The Vao------------          ");
	gotoxy(12,7);
	printf("          Nhap Ma So The : ");
	scannum(tempnum,6,39,7);
	num = atoi(tempnum);
	makeDir(dir,num);
	insertATManimation();
	fp=fopen(dir,"rb");
	fread(&khach,sizeof(khach),1,fp);
	fclose(fp);
	if(fp == NULL){		//kiem tra xem da ton tai file chua
		gotoxy(12,6);
		printf("          ------------Dua The Vao------------          ");
		gotoxy(12,7);
		printf("           The Chua Duoc Tao Hoac Da Bi Xoa            ");
		pushATManimation();
		return 0;
	}
	else if(khach.active == 0 || khach.active == 2){	//ACC chua kich hoat hoac bi khoa
		if(khach.active == 0){
			gotoxy(12,6);
			printf("             Tai Khoan Chua Duoc Kich Hoat         ");
			gotoxy(12,7);
			printf("      Vui Long Toi Ngan Hang Nap Tien De Kich Hoat ");
			scanchar();
			return 0;
		}
		else if(khach.active == 2){
			gotoxy(12,6);
			printf("                  Tai Khoan Da Bi Khoa         ");
			gotoxy(12,7);
			printf("             Vui Long Toi Ngan Hang Mo Khoa    ");
			scanchar();
			return 0;
		}
	}
		else{
			char input[7];
			int dem=1;
			while(1){
			if(dem>5){
				gotoxy(12,6);
				printf("  Ban Nhap Sai Qua 5 Lan. Tai Khoan Cua Ban Da Bi Khoa ");
				khach.active = 2;
				fp = fopen(dir,"wb");
				fwrite(&khach,sizeof(khach),1,fp);
				fclose(fp);
				scanchar();
				pushATManimation();
				return 0;
			}
			gotoxy(12,6);
			printf("          ------------Nhap Ma Pin------------          ");
			dem++;
			gotoxy(12,7);
			printf("          Ma Pin :                                     ");
			scanpin(input,7,32,7);
			MenuPadShow(1);
			gotoxy(12,6);
			printf("                 .....Dang Xac Thuc.                   ");
			GraphAnimation(48,6);
			gotoxy(12,6);
			printf("                                                       ");
			if(strcmp(input,khach.pin) != 0){
				gotoxy(12,8);
				printf("         Nhap Sai. Nhap Sai Qua 5 Lan Se Bi Khoa       ");
				gotoxy(12,9);
				printf("              Nhan Phim Bat Ky De Nhap Lai             ");
				if(dem <= 5){
					scanchar();
				}
				gotoxy(12,8);
				printf("                                                       ");
				gotoxy(12,9);
				printf("                                                       ");
			}
			else {
				MenuPadShow(0);
				gotoxy(12,6);
				printf("   Dang Nhap Thanh Cong. Nhan Phim Bat Ky De Tiep Tuc  ");
				scanchar();
				if(khach.BoolThongbao == 1){
					khach.BoolThongbao = 0;
					Notification();
					gotoxy(17,6);
					printf("%s",khach.thongBao);
					fp = fopen(dir,"wb");
					fwrite(&khach,sizeof(khach),1,fp);
					fclose(fp);
					scanchar();
				}
				return 1;
			}
			fclose(fp);
		}
}
}

int kttk(char *dir){      // ham kiem tra tai khoan ATM, in ra cac thong tin
	FILE *fp;
	khachHang temp;
	fp = fopen(dir,"rb");
	fread(&temp,sizeof(temp),1,fp);
	fclose(fp);
	MenuPadShow(1);
	//strcpy("ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿");
	gotoxy(12,6);
	printf("          So Du Trong Tai Khoan : %10d   ",temp.soDu);
	gotoxy(12,7);
	printf("   Lan Giao Dich Gan Nhat : %20s  ",temp.time);
	if(scanchar() == 27) return 1;
	printLog(dir,temp);
	strcpy(temp.time,getTime());
	sprintf(temp.trangThai,"Kiem Tra Tai Khoan");
	fp = fopen(dir,"wb");
	fwrite(&temp,sizeof(temp),1,fp);
	fclose(fp);
	inPhieu(dir,temp.trangThai,1);
	return 0;
}

int rutTien(char *dir){		// ham rut tien tai khoan ATM
	unsigned int tien;
	FILE *fp;
	khachHang temp;
	char temptien[11];
	fp = fopen(dir,"rb");
	fread(&temp,sizeof(temp),1,fp);
	fclose(fp);
	MenuPadShow(3);
	tien = MenuTien();
	if(tien == 0 || tien == 1){
		if(tien == 1){
			return 1;
		}
		else{
			MenuPadShow(3);
			gotoxy(12,6);
			printf("   Nhap So Tien Muon Rut(Toi Thieu 50000) :            ");
			scannum(temptien,10,55,6); tien = atoi(temptien);
		}
	}
	if(tien > temp.soDu){		// so du nho hon thi nhap lai so tien can rut
		MenuPadShow(3);
		gotoxy(12,6);
		printf("                    So Du Khong Du                     ");
		gotoxy(12,7);
		printf("            Nhan Phim Bat Ky De Quay Ve Menu           ");
		scanchar();
		return 0;
	}
	else if(tien % 50000 != 0 && tien < 50000){		// so du nho hon 10000 thi nhap lai so tien can rut
		MenuPadShow(3);
		gotoxy(12,6);
		printf("                 So Tien Khong Hop Le                  ");
		gotoxy(12,7);
		printf("            Nhan Phim Bat Ky De Quay Ve Menu           ");
		scanchar();
		return 0;
	}
	else{
		MenuPadShow(3);
		gotoxy(12,6);
		printf("              Ban Co Muon Rut So Tien Nay              ");
		if(yesNoAnimation() == 1){
			MenuPadShow(3);
			temp.soDu -= tien;
			strcpy(temp.time,getTime());
			gotoxy(12,6);
			printf("           ...Dang Thuc Hien Rut Tien.                 ");
			fp = fopen(dir,"wb");
			fwrite(&temp,sizeof(temp),1,fp);
			fclose(fp);
			GraphAnimation(50,6);
			gotoxy(12,8);
			printf("           ...Xong........................             ");
			Sleep(1000);
			MenuPadShow(3);
			gotoxy(12,6);
			printf("         So Du Trong Tai Khoan Cua Ban : %-10d",temp.soDu);
			gotoxy(12,8);
			printf("         >> Nhan Tien : Nhan Mot Phim Bat Ky <<        ");
			scanchar();
			Sleep(500);
		    NhanTien(tien);
			sprintf(temp.trangThai,"Da Rut %dVND",tien);
			fp = fopen(dir,"wb");
			fwrite(&temp,sizeof(temp),1,fp);
			fclose(fp);
			inPhieu(dir,temp.trangThai,3);
			printLog(dir,temp);
			sprintf(temp.trangThai,"-   %d",tien);
			printUserLog(dir,temp);
			return 0;
		}
		else{
			system("cls");
			return 0;
		}
	}
}

int chuyenKhoan(char* dir){		// chuyen khoan (tuong tu rut tien)
	int i = 0,num = 0;
	unsigned int tien;
	char desName[15],desDir[30],tempTThai[50],temptien[12];		// des = destination ( tai khoan can chuyen )
	FILE *fp;							// name la soTk, Dir la ten file, vd : acc1.dat
	khachHang temp,desTemp;				// temp la cua tai khoan chuyen, desTemp la tai khoan duoc chuyen
	fp = fopen(dir,"rb");				// ghi cac du lieu can thiet vao temp
	fread(&temp,sizeof(temp),1,fp);
	fclose(fp);
	MenuPadShow(4);
	gotoxy(12,6);
	printf("       So Du Trong Tai Khoan Cua Ban : %-14d",temp.soDu);
	gotoxy(12,7);
	printf("       Nhap Tai Khoan Muon Chuyen :                    ");
	fflush(stdin); scannum(desName,13,48,7);
	for(i = 0;i <6;i++){		//gan chuoi 2221995xxxxx thanh xxxxx NULL 5xxxx
		desName[i] = desName[i+7];	//muc dich de lay 5 so cuoi
	}
	num = atoi(desName);			//chuyen alpha thanh integer
	makeDir(desDir,num);			//tao duong dan (ten file) tu bien num
	if((fp=fopen(desDir,"rb")) == NULL){		//kiem tra xem da ton tai file chua
		fclose(fp);
		MenuPadShow(4);
		gotoxy(12,6);
		printf("                   The Khong Ton Tai                   ");
		scanchar();
		return 1;
		}
	else if(strcmp(desDir,dir)==0){
		fclose(fp);
		MenuPadShow(4);
		gotoxy(12,6);
		printf("        The Duoc Chuyen Trung Voi The Chuyen Tien      ");
		scanchar();
		return 1;
	}
	else{
		fread(&desTemp,sizeof(desTemp),1,fp);
		fclose(fp);
	}
	MenuPadShow(4);
	tien = MenuTien();
	if(tien == 0 || tien == 1){
		if(tien == 1){
			return 1;
		}
		else{
			gotoxy(12,6);
			MenuPadShow(4);
			gotoxy(12,6);
			printf(" Nhap So Tien Muon Chuyen(Toi Thieu 50000) :           ");
			scannum(temptien,10,57,6); tien = atoi(temptien);
		}
	}
	if(tien > temp.soDu){		// so du nho hon thi nhap lai so tien can rut
		MenuPadShow(4);
		gotoxy(12,6);
		printf("                    So Du Khong Du                     ");
		gotoxy(12,7);
		printf("            Nhan Phim Bat Ky De Quay Ve Menu           ");
		scanchar();
		return 1;
	}
	else if(tien % 50000 != 0 && tien < 50000){		// so du nho hon 10000 thi nhap lai so tien can rut
		MenuPadShow(4);
		gotoxy(12,6);
		printf("                 So Tien Khong Hop Le                  ");
		gotoxy(12,7);
		printf("            Nhan Phim Bat Ky De Quay Ve Menu           ");
		scanchar();
		return 1;
	}
	else{
		MenuPadShow(4);
		gotoxy(12,6);
		printf("                   So Tien Hop Le                      ");
		gotoxy(12,7);
		printf("            Ban Co Muon Chuyen So Tien Nay             ");
		if(yesNoAnimation() == 1){
			MenuPadShow(4);
			temp.soDu -= tien;
			strcpy(temp.time,getTime());	//cap nhat du lieu cho tai khoan chuyen tien
			strcpy(desTemp.time,getTime());	//cap nhat du lieu cho tai khoan duoc chuyen tien
			desTemp.soDu += tien;				
			sprintf(desTemp.trangThai,"Da Nhan Tu Tai Khoan %s %dVND",temp.soTk,tien);
			sprintf(desTemp.thongBao,"Nhan %dVND Tu Tai Khoan %s",tien,temp.soTk);
			desTemp.BoolThongbao = 1;			
			printLog(desDir,desTemp);
			sprintf(desTemp.trangThai,"+   %d",tien);
			printUserLog(desDir,desTemp);
			gotoxy(12,6);
			printf("            ...Dang Chuyen..........                   ");
			fp = fopen(desDir,"wb");
			fwrite(&desTemp,sizeof(desTemp),1,fp);
			fclose(fp);
			GraphAnimation(48,6);
			gotoxy(12,7);
			printf("            ...Xong.....................               ");
			Sleep(1000);
			MenuPadShow(4);
			gotoxy(12,6);
			printf("      So Du Trong Tai Khoan Cua Ban : %d",temp.soDu);
			scanchar();
			sprintf(temp.trangThai,"Chuyen Cho TK %s %dVND",desTemp.soTk,tien);
			fp = fopen(dir,"wb");
			fwrite(&temp,sizeof(temp),1,fp);
			fclose(fp);
			inPhieu(dir,temp.trangThai,4);
			printLog(dir,temp);
			sprintf(temp.trangThai,"-   %d",tien);
			printUserLog(dir,temp);
			return 0;
		}
	}
}

int doiMaPin(char* dir){
	char mapinbandau[7],mapin[7],xacnhan[7];	//mapin va xacnhan... dung de xac nhan mat khau
	FILE *fp;
	khachHang temp;
	int dem = 1;
	fp = fopen(dir,"rb");
	fread(&temp,sizeof(temp),1,fp);		//doc cac gia tri can thiet tu file
	fclose(fp);
	strcpy(mapinbandau,temp.pin);
	while(1){
		if(dem > 5){		// dieu kien nhu o duoi
			printf("\n Ban Da Nhap Sai Qua 5 Lan...\n");
			Sleep(1000);
			printf("\n Chuong Trinh Tu Dong Thoat...\n\n");
			return 1;
		}
		MenuPadShow(5);
		gotoxy(12,9);
		printf("          Nhap Ma PIN Hien Tai :                       ");
		fflush(stdin); scanpin(mapin,7,46,9);
		if(strcmp(mapin,temp.pin) != 0){	// neu khong dung thi nhap lai
			dem++;
			gotoxy(12,9);
			printf("      Ma Pin Sai. Nhan Phim Bat Ky De Nhap Lai         ");
			scanchar();
			continue;
		}
		else{
			while(1){
				MenuPadShow(5);
				gotoxy(12,9);
				printf("          Nhap Ma PIN Moi      :                       ");
				fflush(stdin); scanpin(mapin,7,46,9);
				if(strlen(mapin) < 6){
					gotoxy(12,9);
					printf("          >>Ma Pin Phai Day Du 6 Chu So<<              ");
					gotoxy(12,10);
					printf("            Nhan Phim Bat Ky De Nhap Lai               ");
					scanchar();
					gotoxy(12,10);
					printf("                                                       ");
					gotoxy(12,11);
					printf("                                                       ");
					continue;
				}
				gotoxy(12,9);
				printf("          Xac Nhan Ma PIN Moi  :                       ");
				fflush(stdin); scanpin(xacnhan,7,46,9);
				if(strcmp(mapin,xacnhan) != 0){			// neu khong trung thi nhap lai
					gotoxy(12,9);
					printf(" Ma Pin Khong Trung Khop. Nhan Phim Bat Ky De Nhap Lai ");
					scanchar();
					continue;	
				}
				else{									// trung thi doi ma pin
					gotoxy(12,9);
					printf("          ...Dang Doi Ma Pin......                     ");
					GraphAnimation(46,9);
					strcpy(temp.pin,mapin);
					strcpy(temp.time,getTime());
					fp = fopen(dir,"wb");
					fwrite(&temp,sizeof(temp),1,fp);	//cap nhat ma pin cho file
					fclose(fp);
					gotoxy(12,9);
					printf("          ...Xong.....................                 ");
					Sleep(1000);
					sprintf(temp.trangThai,"Doi Ma Pin Tu %s Sang %s",mapinbandau,temp.pin);
					fp = fopen(dir,"wb");
					fwrite(&temp,sizeof(temp),1,fp);
					fclose(fp);
					printLog(dir,temp);
					return 0;
				}
			}
		}
	}
}

int saoKeTk(char* diruser){	
	int num;
	FILE *fp;
	char dir[30];
	khachHang temp;
	Nhap:
	MenuPadShow(6);
	strcpy(dir,diruser);
	dir[strlen(dir) - 4] = NULL;
	strcat(dir,"_log_user.dat");
	if((fp=fopen(dir,"rb")) == NULL){
		fclose(fp);
		gotoxy(12,9);
		printf("      Tai Khoan Hien Chua Co Bat Ky Giao Dich Nao      ");
		Sleep(3000);
		return 1;
		}
	else{
		int count = 0,y = 6;
		while(count < 6){
			fread(&temp,sizeof(temp),1,fp);
			temp.time[strlen(temp.time)-1] = ' ';
			gotoxy(17,y++);
			if(!feof(fp)){
				printf("%s  %s",temp.time,temp.trangThai);
				count++;	
			}else{
				scanchar();
				break;
			}
			if(count == 6){
					gotoxy(60,12);
					printf("ÚÄÄÄÄ¿");
					gotoxy(60,13);
					printf("³NEXT³");
					gotoxy(60,14);
					printf("ÀÄÄÄÄÙ");
					count = 0;
					y = 6;
					while(scanchar() != 'd' ){
						continue;
					}
					MenuPadShow(6);
			}
		}	
		MenuPadShow(6);
		gotoxy(17,9);
		printf("     Nhan Phim Bat Ky De Quay Ve Menu");
		getch();
		return 1;
	}
}

void menuGuestShow(char* hoten){
	gotoxy(12,3);
	printf("                 Xin Chao %-25s",hoten);
	gotoxy(12,4);
	printf("² ²²²²² ²²² ²²²     ²²²²       ²²²²²² ²²²²²² ²²²²²²² ²²");
	gotoxy(12,5);
	printf("²² ²²² ²²²² ²²² ²²²² ²²²²²² ²²²²²²² ²²² ²²²² ² ²²² ² ²²");
	gotoxy(12,6);
	printf("²²² ² ²²²²² ²²²     ²²²²²²² ²²²²²²       ²²² ²²² ²²² ²²");
	gotoxy(12,7);
	printf("²²²² ²²²²²² ²²² ²²²²²²²²²²² ²²²²² ²²²²²²² ²² ²²²²²²² ²²");
	gotoxy(12,8);
	printf(" ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿             ÚÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ¿ ");
	gotoxy(12,9);
	printf(" ³Kiem Tra Tai Khoan³             ³     Rut Tien     ³ ");
	gotoxy(12,10);
	printf(" %cÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ´             %cÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ´ ",195,195);
	gotoxy(12,11);
	printf(" ³ Chuyen Khoan     ³             ³    Doi Ma Pin    ³ ");
	gotoxy(12,12);
	printf(" %cÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ´             %cÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ´ ",195,195);
	gotoxy(12,13);
	printf(" ³ Sao Ke TK        ³             ³       Thoat      ³ ");
	gotoxy(12,14);
	printf(" ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ             ÀÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÙ ");
	
}
void menuGuest(char *dir){
	FILE *fp;
	khachHang temp;
	fp = fopen(dir,"rb");
	fread(&temp,sizeof(temp),1,fp);		// doc cac thong tin can thiet tu file
	fclose(fp);
	int choice;				// bien lua chon switch case
	do{
	MenuPadShow(0);
	menuGuestShow(temp.tenTk);
	fflush(stdin);
	choice = scanchar();
	switch (choice){
		case 'q' :
			if(kttk(dir) == 1) continue;
			MenuPadShow(7);
			gotoxy(21,9); printf("Ban Co Muon Thuc Hien Tiep Giao Dich");
			if(yesNoAnimation() == 1){
				choice = 0; // de quay ve menu, thoa dieu kien vong lap
				continue;
			}
			else{
				MenuGoodbye();
				pushATManimation();
				break;
			}
		case 'a' :
			if(rutTien(dir) == 1) continue;
			MenuPadShow(7);
			gotoxy(21,9); printf("Ban Co Muon Thuc Hien Tiep Giao Dich");
			if(yesNoAnimation() == 1){
				choice = 0; // de quay ve menu, thoa dieu kien vong lap
				continue;
			}
			else{
				MenuGoodbye();
				pushATManimation();
				break;
			}
		case 'w' :
		if(chuyenKhoan(dir) == 1) continue;
			MenuPadShow(7);
			gotoxy(21,9); printf("Ban Co Muon Thuc Hien Tiep Giao Dich");
			if(yesNoAnimation() == 1){
				choice = 0; // de quay ve menu, thoa dieu kien vong lap
				continue;
			}
			else{
				MenuGoodbye();
				pushATManimation();
				break;
			}
		case 's' :
		if(doiMaPin(dir) == 1) return;
			MenuPadShow(7);
			gotoxy(21,9); printf("Ban Co Muon Thuc Hien Tiep Giao Dich");
			if(yesNoAnimation() == 1){
				choice = 0; // de quay ve menu, thoa dieu kien vong lap
				continue;
			}
			else{
				MenuGoodbye();
				pushATManimation();
				break;
				}
		case 'e' :
		if(saoKeTk(dir) == 1) continue;
			MenuPadShow(7);
			gotoxy(21,9); printf("Ban Co Muon Thuc Hien Tiep Giao Dich");
			if(yesNoAnimation() == 1){
				choice = 0; // de quay ve menu, thoa dieu kien vong lap
				continue;
			}
			else{
				pushATManimation();
				MenuGoodbye();
				break;
			}
		case 'd' :
			MenuGoodbye();
			pushATManimation();
			break;
		default:
			choice = 0;
			continue;
	}
	return ; 
	}
	while (choice > 6 || choice < 1);
}
//CHUONG TRINH MO PHONG ATM


//======================================================================================================


//CHUONG TRINH QUAN LY TAI KHOAN (them createAcc)

int	createAcc(){	// ham tao tai khoan
	FILE *fp;
	char dir[30];
	khachHang khach,temp;
	int stt;
	makeDir(dir,stt=readnum("CSDL.txt",1));		// tao ten duong dan (ten file) VD : acc1.dat, acc2.dat ....
	makesoTk(khach.soTk,readnum("CSDL.txt",0) - 1); //tao so tai khoan voi dinh dang 2221995xxxxx
	khach.soDu= 50000;
	Menu:
	printf("\n==================Tao Tai Khoan ATM==================\n");
	printf("\n Nhap Ho Ten : "); fflush(stdin); gets(khach.tenTk);
	printf("\n Nhap Ma PIN : ");
	while(1){
		getpin(khach.pin,7);
		if(strlen(khach.pin) < 6){
			printf("\n Khong Du 6 Chu So. Nhan Phim Bat Ky De Nhap Lai Ma PIN\n");
			getch();
			system("cls");
			printf("\n==================Tao Tai Khoan ATM==================\n");
			printf("\n Nhap Ho Ten : %s\n",khach.tenTk);
			printf("\n Nhap Ma PIN : ");
		}
		else{
			break;
		}
	}
	strcpy(khach.time,getTime());
	khach.active = 0;
	printf("\n\n");
	strcpy(khach.trangThai,"Tao Tai Khoan");
	printInfo(khach,1,khach.trangThai);
	printf("\n Dong Y Tao Tai Khoan ? (Y/N)\n");
	if(yesNo()==1) goto TaoTk;
	else{
		system("cls");
		goto Menu;
	}
	TaoTk:
	fp=fopen(dir,"wb");
	fwrite(&khach,sizeof(khach),1,fp);
	fclose(fp);
	printf("\n ..Dang Tao..");
	animation();
	printf("\n\n Tao Tai Khoan Thanh Cong\n");
	getch();
	return stt;		//tra ve so thu tu cua file vd: acc1.dat thi stt = 1
}

void editAcc(){
	int num;
	FILE *fp;
	char dir[30];
	khachHang khach;
	Nhap:
	system("cls");
	printf("\n==================Sua Tai Khoan ATM==================\n");
	printf("\n #Nhap Ma So The : ");
	scanf("%d",&num);
	makeDir(dir,num);
	if((fp=fopen(dir,"rb")) == NULL){
		fclose(fp);
		int choice;
		do{
			printf("\n Account Nay Khong Ton Tai. Ban Muon\n");
			printf("\n ---1.Nhap Ma So The Khac\n");
			printf("\n ---2.Tro Ve Menu\n");
			printf("\n #Chon : ");
			fflush(stdin); scanf("%d",&choice);
			switch (choice){
				case 1 :
					system("cls");
					goto Nhap;
					break;
				case 2 :
					return;
				default :
				system("cls");
				printf("\n==================Sua Tai Khoan ATM==================\n");
				printf("\n #Nhap Ma So The : %d\n",num);
				break;
			}
		}while(choice > 2 || choice < 1 );		// kiem tra da co file chua
	}
	else{
		fread(&khach,sizeof(khach),1,fp);		//tuong tu createAcc
		fclose(fp);
		Menu:
		printf("\n Nhap Ho Ten : "); fflush(stdin); gets(khach.tenTk);
		printf("\n Nhap Ma PIN : ");
		while(1){
			getpin(khach.pin,7);
			if(strlen(khach.pin) < 6){
				printf("\n Khong Du 6 Chu So. Nhan Phim Bat Ky De Nhap Lai Ma PIN\n");
				getch();
				system("cls");
				printf("\n==================Sua Tai Khoan ATM==================\n");
				printf("\n #Nhap Ma So The : %d\n",num);
				printf("\n Nhap Ho Ten : %s\n",khach.tenTk);
				printf("\n Nhap Ma PIN : ");
			}
			else{
				break;
			}
		}
		printf("\n Nhap So Du : ");
		scanf("%d",&khach.soDu);
		strcpy(khach.time,getTime());
		printf("\n\n");
		printInfo(khach,1,"Sua Tai Khoan");
		printf("\n Dong Y Sua Tai Khoan ? (Y/N)\n");
		if(yesNo()==1) goto SuaTk;
		else{
			system("cls");
			printf("\n==================Sua Tai Khoan ATM==================\n");
			printf("\n #Nhap Ma So The : %d\n",num);
			goto Menu;
		}
	SuaTk:
	fp=fopen(dir,"wb");
	fwrite(&khach,sizeof(khach),1,fp);
	fclose(fp);
	printf("\n ..Dang Sua..");
	animation();
	printf("\n\n Sua Tai Khoan Thanh Cong\n");
	getch();
	system("cls");
	return ;
	}
}
void deleteAcc(){
	int num;
	FILE *fp;
	char dir[30],dirLog[30];
	khachHang khach;
	strcpy(dirLog,dir);
	dirLog[strlen(dirLog) - 4] = NULL;
	strcat(dirLog,"_log_user.dat");
	Nhap:
	system("cls");
	printf("\n==================Xoa Tai Khoan ATM==================\n");
	printf("\n #Nhap Ma So The : ");
	scanf("%d",&num);
	makeDir(dir,num);
	if((fp=fopen(dir,"rb")) == NULL){
		fclose(fp);
		int choice;
		do{
			printf("\n Account Nay Khong Ton Tai. Ban Muon\n");
			printf("\n ---1.Nhap Ma So The Khac\n");
			printf("\n ---2.Tro Ve Menu\n");
			printf("\n #Chon : ");
			fflush(stdin); scanf("%d",&choice);
			switch (choice){
				case 1 :
					system("cls");
					goto Nhap;
					break;
				case 2 :
					return;
				default :
				system("cls");
				printf("\n==================Sua Tai Khoan ATM==================\n");
				printf("\n #Nhap Ma So The : %d\n",num);
				break;
			}
		}while(choice > 2 || choice < 1 );		// kiem tra da co file chua
	}
	else{
		fread(&khach,sizeof(khach),1,fp);		//tuong tu createAcc
		fclose(fp);
		printf("\n\n");
		printInfo(khach,1,"Xoa Tai Khoan");
		printf("\n Dong Y Xoa Tai Khoan ? (Y/N)\n");
		if(yesNo()==1){
			printf("\n..Dang Xoa..");
			animation();
			remove(dirLog) == 0;
			if(remove(dir) == 0 )
				printf("\n\n Xoa Thanh Cong ");	
			else{
				printf("\n\n Xay Ra Loi Trong Qua Trinh Xoa");
			}
			getch();
		}
		else{
			return;
		}
	}
}

int active(){		//active account.
	int num;
	FILE *fp;
	char dir[30];
	khachHang khach;
	Nhap:
	system("cls");
	printf("\n====================Active Account====================\n");
	printf("\n #Nhap Ma So The : ");
	scanf("%d",&num);
	makeDir(dir,num);
	if((fp=fopen(dir,"rb")) == NULL){
		fclose(fp);
		int choice;
		do{
			printf("\n Account Nay Khong Ton Tai. Ban Muon\n");
			printf("\n ---1.Nhap Ma So The Khac\n");
			printf("\n ---2.Tro Ve Menu\n");
			printf("\n #Chon : ");
			fflush(stdin); scanf("%d",&choice);
			switch (choice){
				case 1 :
					system("cls");
					goto Nhap;
					break;
				case 2 :
					return 0;
				default :
				system("cls");
				printf("\n====================Active Account====================\n");
				printf("\n #Nhap Ma So The : %d\n",num);
				break;
			}
		}while(choice > 2 || choice < 1 ); //kiem tra su ton tai cua tai khoan
	}
	else{	//active account
		fread(&khach,sizeof(khach),1,fp);
		fclose(fp);
		if(khach.active	== 1){		
			printf("\n Tai Khoan Da Duoc Active Roi\n");
			printf("\n Nhan Phim Bat Ky De Quay Ve Menu\n");
			getch();
			return 0;
		}
		printf("\n\n");
		printInfo(khach,0,"Non Actived Account");
		printf("\n Dong Y Active Tai Khoan Nay (Y/N)\n");
		if(yesNo() == 1){
			khach.active = 1;
			strcpy(khach.time,getTime());
			strcpy(khach.trangThai,"Active");
			fp = fopen(dir,"wb");
			fwrite(&khach,sizeof(khach),1,fp);
			fclose(fp);
			printLog(dir,khach);
			printf("\n\n Active Thanh Cong");
			getch();
			return 1;
		}
		else{
			system("cls");
			goto Nhap;
		}
	}
}

int blockacc(){		//block account.
	int num;
	FILE *fp;
	char dir[30];
	khachHang khach;
	Nhap:
	system("cls");
	printf("\n====================Block Account=====================\n");
	printf("\n #Nhap Ma So The : ");
	scanf("%d",&num);
	makeDir(dir,num);
	if((fp=fopen(dir,"rb")) == NULL){
		fclose(fp);
		int choice;
		do{
			printf("\n Account Nay Khong Ton Tai. Ban Muon\n");
			printf("\n ---1.Nhap Ma So The Khac\n");
			printf("\n ---2.Tro Ve Menu\n");
			printf("\n #Chon : ");
			fflush(stdin); scanf("%d",&choice);
			switch (choice){
				case 1 :
					system("cls");
					goto Nhap;
					break;
				case 2 :
					return 0;
				default :
				system("cls");
				printf("\n====================Active Account====================\n");
				printf("\n #Nhap Ma So The : %d\n",num);
				break;
			}
		}while(choice > 2 || choice < 1 ); //kiem tra su ton tai cua tai khoan
	}
	else{	//active account
		fread(&khach,sizeof(khach),1,fp);
		fclose(fp);
		if(khach.active	!= 1){		
			printf("\n Tai Khoan Da Duoc Block Roi\n");
			printf("\n Nhan Phim Bat Ky De Quay Ve Menu\n");
			getch();
			return 0;
		}
		printf("\n\n");
		printInfo(khach,0,"Non Actived Account");
		printf("\n Dong Y Block Tai Khoan Nay (Y/N)\n");
		if(yesNo() == 1){
			khach.active = 2;
			strcpy(khach.time,getTime());
			strcpy(khach.trangThai,"Blocked");
			fp = fopen(dir,"wb");
			fwrite(&khach,sizeof(khach),1,fp);
			fclose(fp);
			printLog(dir,khach);
			printf("\n\n Block Thanh Cong");
			getch();
			return 1;
		}
		else{
			system("cls");
			goto Nhap;
		}
	}
}

int napTien(){		
	int num;
	FILE *fp;
	char dir[30],diruser[30];
	khachHang khach;
	unsigned int tien;
	Nhap:
	system("cls");
	printf("\n====================Nap Tien====================\n");
	printf("\n #Nhap Ma So The : ");
	scanf("%d",&num);
	makeDir(dir,num);
	if((fp=fopen(dir,"rb")) == NULL){
		fclose(fp);
		int choice;
		do{
			printf("\n Account Nay Khong Ton Tai\n");
			printf("\n ---1.Nhap Ma So The Khac\n");
			printf("\n ---2.Tro Ve Menu\n");
			printf("\n #Chon : ");
			fflush(stdin); scanf("%d",&choice);
			switch (choice){
				case 1 :
					system("cls");
					goto Nhap;
					break;
				case 2 :
					return 0;
				default :
				system("cls");
				printf("\n====================Nap Tien====================\n");
				printf("\n #Nhap Ma So The : %d\n",num);
				break;
			}
		}while(choice > 2 || choice < 1 ); //kiem tra su ton tai cua tai khoan
	}
	else{
		fread(&khach,sizeof(khach),1,fp);
		fclose(fp);
		if(khach.active	== 2){
			printf("\n Tai Khoan Dang Bi Khoa\n");
			printf("\n Xin Hay Mo Khoa Account Truoc Khi Nap");
			printf("\n Nhan Phim Bat Ky De Quay Ve Menu\n");
			getch();
			return 0;
		}
		while(1){
			printf("\n Nhap So Tien Muon Nap (Toi Thieu 50000) : ");
			scanf("%d",&tien);
			if(tien % 50000 || tien < 50000){		// nap it nhat 50000
				printf("\n So Tien Khong Hop Le. Ban Co Muon Nhap Lai So Tien Muon Nap (Y/N)\n");
				if(yesNo() == 1){
					system("cls");
					printf("\n====================Nap Tien====================\n");
					printf("\n #Nhap Ma So The : %d\n",num);
					continue;
				}
				else{
					return 0;
				}
			}
			else{
					printf("\n Ban Co Muon Nap So Tien Nay (Y/N)\n");
					if(yesNo() == 1){
						khach.soDu += tien;
						strcpy(khach.time,getTime());
						khach.active = 1;
						strcpy(khach.trangThai,"Active");
						sprintf(khach.thongBao,"Tai Khoan Vua Moi Nap %d VND",tien);
						khach.BoolThongbao = 1;
						printf("\n ...Dang Thuc Hien Nap Tien.");	
						fp = fopen(dir,"wb");
						animation();
						printf("\n\n ...Xong........................\n");
						printf("\n So Du Trong Tai Khoan Cua Ban : %d\n",khach.soDu);
						sprintf(khach.trangThai,"Da Nap %dVND",tien);
						fwrite(&khach,sizeof(khach),1,fp);
						fclose(fp);
						printLog(dir,khach);
						sprintf(khach.trangThai,"+   %d",tien);
						printUserLog(dir,khach);
						getch();
						break;
					}
					else{
						system("cls");
						printf("\n====================Nap Tien====================\n");
						printf("\n #Nhap Ma So The : %d\n",num);
						continue;
					}
			}
		}
	}
}

void ATMmanager(){
	FILE *fp;
	khachHang temp;
	int choice;				// bien lua chon switch case
	do{
	printf("\nÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»");
	printf("\nº                                                      º");
	printf("\nº                  Xin Chao ATM Manager                º");
	printf("\nº                                                      º");
	printf("\nº  ---1.Tao Tai Khoan              ---5.Active Account º");
	printf("\nº                                                      º");
	printf("\nº  ---2.Sua Tai Khoan              ---6.Block Account  º");
	printf("\nº                                                      º");
	printf("\nº  ---3.Xoa Tai Khoan              ---7.Xem File Log   º");
	printf("\nº                                                      º");
	printf("\nº  ---4.Nap Tien                   ---8.Thoat          º");
	printf("\nº                                                      º");
	printf("\nº                                                      º");
	printf("\nÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼\n");
	printf("\n#Chon : ");
	fflush(stdin); scanf("%d",&choice);
	switch (choice){
		case 1 :
			system("cls");
			createAcc();
			system("cls");
			choice = 0; // de quay ve menu, thoa dieu kien vong lap
			continue;
		case 2 :
			editAcc();
			system("cls");
			choice = 0; // de quay ve menu, thoa dieu kien vong lap
			continue;
		case 3 :
			system("cls");
			deleteAcc();
			system("cls");
			choice = 0;
			continue;
		case 4 :
			system("cls");
			napTien();
			system("cls");
			choice = 0;
			continue;
		case 5 :
			system("cls");
			active();
			system("cls");
			choice = 0;
			continue;
		case 6 :
			system("cls");
			blockacc();
			system("cls");
			choice = 0;
			continue;
		case 7 :
			system("cls");
			logReader();
			system("cls");
			choice = 0;
			continue;
		case 8 :
			exit(0);		//thoat chuong trinh
			break;
		default:
			system("cls"); // xoa man hinh, nhap lai
			break;
	}
	}
	while (choice > 8 || choice < 1);
}
//CHUONG TRINH QUAN LY TAI KHOAN



//=======================================================================================================

	
/*MENU*/
		
void menu(char* dir){
	int choice;
	do{
		printf(" .----------------.  .----------------.  .----------------. \n");
		printf("| .--------------. || .--------------. || .--------------. |\n");
		printf("| |      __      | || |  _________   | || | ____    ____ | |\n");
		printf("| |     /  \\     | || | |  _   _  |  | || ||_   \\  /   _|| |\n");
		printf("| |    / /\\ \\    | || | |_/ | | \\_|  | || |  |   \\/   |  | |\n");
		printf("| |   / ____ \\   | || |     | |      | || |  | |\\  /| |  | |\n");
		printf("| | _/ /    \\ \\_ | || |    _| |_     | || | _| |_\\/_| |_ | |\n");
		printf("| ||____|  |____|| || |   |_____|    | || ||_____||_____|| |\n");
		printf("| |              | || |              | || |              | |\n");
		printf("| '--------------' || '--------------' || '--------------' |\n");
		printf(" '----------------'  '----------------'  '----------------' \n");
		printf("       _____ _____ _____ __    _____ _____ _____ _____ \n");
		printf("      |   __|     |  |  |  |  |  _  |_   _|     | __  |\n");
		printf("      |   __| | | |  |  |  |__|     | | | |  |  |    -|\n");
		printf("      |_____|_|_|_|_____|_____|__|__| |_| |_____|__|__|\n");
		printf("                                                 \n");
		printf("      =======================BY========================\n");
		printf("      ==================VU==QUANG==TAM=================\n");
		printf("      =====================A=T=9=D=====================\n");
		printf("\n---1.ATM Account Manager\n");
		printf("\n---2.ATM For Using\n");
		printf("\n---3.Exit\n");
		printf("\nChoose : ");
		fflush(stdin); scanf("%d",&choice);
		switch (choice){
		case 1 :
			system("cls");
			ATMmanager();
		case 2 :
			system("cls");
			while(1){
				MenuWelcome();
				if(MenuLanguage() == 0) {
					MenuPadShow(0);
					gotoxy(12,9);
					printf("            Ngon Ngu Nay Hien Dang Xay Dung            ");
					Sleep(3000);
				}
				else if(insertATM(dir)){
						system("cls");
						menuGuest(dir);
				}
			}
		case 3 :
			exit(0);		//thoat chuong trinh
		default:
			system("cls"); // xoa man hinh, nhap lai
			break;
		}
	}while(choice > 2 || choice < 1);
	getch();
}

