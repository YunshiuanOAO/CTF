#include<stdio.h>
#include<stdlib.h>
int a1[9] = {0x0e,0x0d,0x7d,0x06,0x0f,0x17,0x76,0x04};

char f(int a1, int a2){
  for(int i=65;i<91;i++){
    int v2; 
    int v4; 
    int v5; 
    v5 = (17 * a2 + i - 65) % 26;
    v4 = a2 % 3 + 3;
    v2 = a2 % 3;
    if ( a2 % 3 == 2 )
    {
        v5 = (v5 - v4 + 26) % 26;
    }
    else if ( v2 <= 2 )
    {
        if ( v2 )
        {
        if ( v2 == 1 )
            v5 = (2 * v4 + v5) % 26;
        }
        else
        {
        v5 = (v4 * v5 + 7) % 26;
        }
    }
    if(v5+65 == a1)return (char)i;
  }
}

void xor_strings(char* a,int *d) {
    for(int i=0;i<=7;i++){
        a[i] = (char)(d[i]^a[i]);
    }
}
int main(){
    char a[8] = "DHLIYJEG";
    char b[8] = "MZRERYND";
    char c[8] = "RUYODBAH";
    char d[8] = "BKEMPBRE";
    int a1[9] = {0x0e,0x0d,0x7d,0x06,0x0f,0x17,0x76,0x04};
    int b1[9] = {0x6d,0x00,0x1b,0x7c,0x6c,0x13,0x62,0x11};
    int c1[9] = {0x1e,0x7e,0x06,0x13,0x07,0x66,0x0e,0x71};
    int d1[9] = {0x17,0x14,0x1d,0x70,0x79,0x67,0x74,0x33};
    for(int i=0;i<=7;i++){
        a[i] = f(a[i],i);
        b[i] = f(b[i],i+32);
        c[i] = f(c[i],i+64);
        d[i] = f(d[i],i+96);
        printf("%c %c %c %c\n",a[i],b[i],c[i],d[i]);
    }
    xor_strings(a,a1);
    xor_strings(b,b1);
    xor_strings(c,c1);
    xor_strings(d,d1);
    for(int i=0;i<=7;i++){
        printf("%c",a[i]);
    }
    for(int i=0;i<=7;i++){
        printf("%c",b[i]);
    }
    for(int i=0;i<=7;i++){
        printf("%c",c[i]);
    }
    for(int i=0;i<=7;i++){
        printf("%c",d[i]);
    }
}