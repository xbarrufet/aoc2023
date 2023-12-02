#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// #define FILENAME "sample.txt"
//#define FILENAME "sample2.txt"
#define FILENAME "input.txt"


int procesaLinea(char *linia, int len)
{
    int primer = -1;
    int ultim = -1;
    for (int t = 0; t < len; t++)
    {
        if (isdigit(linia[t]))
        {
            if (primer < 0)
            {
                primer = (int)linia[t] - 48;
            }
            ultim = (int)linia[t] - 48;
        }
    }
    printf("------%d ` %d = %d\n", primer, ultim, primer * 10 + ultim);
    return primer * 10 + ultim;
}

int main()
{

    FILE *fp;
    ssize_t read;

    char *linia = NULL;

    // tamany de la linia
    size_t len_read = 0;
    int len=0;

    // acumulat
    int acum = 0;

    // linia ambs els numeros passats a digits (exercisi B)
    char nova_linia[50];

    // obrim el fitxer en mode lectura
    fp = fopen(FILENAME, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE); // constant definida a stdlib.h

    // anem llegint linia a linia fis que getline torna un -1

    while ((read = getline(&linia, &len_read, fp)) != -1)
    {

            printf("------------------------\n");
            printf("linia %s len:%d strlen:%d\n", linia,(int)len, (int)strlen(linia));
            len = (int)strlen(linia);
        // PROVA A: acum +=procesaLinea(linia,len);
        for (int t = 0; t < len; t++)
        {

            if (len - t > strlen("zero") && linia[t] == 'z' && linia[t + 1] == 'e' && linia[t + 2] == 'r' && linia[t + 3] == 'o')
                nova_linia[t] = '0';
            else if (len - t > strlen("one") && linia[t] == 'o' && linia[t + 1] == 'n' && linia[t + 2] == 'e')
                nova_linia[t] = '1';
            else if (len - t > strlen("two") && linia[t] == 't' && linia[t + 1] == 'w' && linia[t + 2] == 'o')
                nova_linia[t] = '2';
            else if (len - t > strlen("three") && linia[t] == 't' && linia[t + 1] == 'h' && linia[t + 2] == 'r' && linia[t + 3] == 'e' && linia[t + 4] == 'e')
                nova_linia[t] = '3';
            else if (len - t > strlen("four") && linia[t] == 'f' && linia[t + 1] == 'o' && linia[t + 2] == 'u' && linia[t + 3] == 'r')
                nova_linia[t] = '4';
            else if (len - t > strlen("five") && linia[t] == 'f' && linia[t + 1] == 'i' && linia[t + 2] == 'v' && linia[t + 3] == 'e')
                nova_linia[t] = '5';
            else if (len - t > strlen("six") && linia[t] == 's' && linia[t + 1] == 'i' && linia[t + 2] == 'x')
                nova_linia[t] = '6';
            else if (len - t > strlen("seven") && linia[t] == 's' && linia[t + 1] == 'e' && linia[t + 2] == 'v' && linia[t + 3] == 'e' && linia[t + 4] == 'n')
                nova_linia[t] = '7';
            else if (len - t > strlen("eight") && linia[t] == 'e' && linia[t + 1] == 'i' && linia[t + 2] == 'g' && linia[t + 3] == 'h' && linia[t + 4] == 't')
                nova_linia[t] = '8';
            else if (len - t > strlen("nine") && linia[t] == 'n' && linia[t + 1] == 'i' && linia[t + 2] == 'n' && linia[t + 3] == 'e')
                nova_linia[t] = '9';
            else
                nova_linia[t] = linia[t];
            printf("%c", nova_linia[t]);
        }
        acum += procesaLinea(nova_linia, len);
    }
    printf("acumulat es %d", acum);
    fclose(fp);
    if (linia)
        free(linia);
    exit(EXIT_SUCCESS);
}