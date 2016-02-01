#include <stdio.h>
#include <conio.h>
#include <windows.h>

int main(){
	FILE *fp;
	char c;
	Xemlai:
	fp = fopen("picture.txt","r");
	while((c = fgetc(fp)) != EOF ){
		printf("%c",c);
		if (c == '\n')
			Sleep(50);
	}
	fclose(fp);
	printf("\n\n\n\n\n                         An Space De Tiep Tuc Nha Em");
	while(1){
		if (getch() == 32){
			system("cls");
			break;
		}
	} 
	fp = fopen("picture2.txt","r");
	while((c = fgetc(fp)) != EOF ){
		printf("%c",c);
		if (c == '\n')
			Sleep(50);
	}
	fclose(fp);
	printf("\n\n\n\n\n                         An Space De Tiep Tuc Nha Em");
	while(1){
		if (getch() == 32){
			system("cls");
			break;
		}
	} 
	printf("Muon xem lai khong em ? (nhan space de xem lai, nhan phim khac de tiep tuc (con nua :P))");
	if (getch() == 32){
		system("cls");
		goto Xemlai;
	}
	else{
		system("thu.doc");
		exit(1);
	}
}