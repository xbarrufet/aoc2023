#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

//#define FILENAME "sample.txt"
// #define FILENAME "sample2.txt"
#define FILENAME "input.txt"

#define SIZE_BOARD 10
#define SIZE_BOARD 140

#define CODI '.'

int numero(char c)
{
    return (int)c - 48;
}


char * copia_linia(char board[SIZE_BOARD][SIZE_BOARD], int linia) {
    char * result = calloc(SIZE_BOARD, sizeof(char));
    for(int t=0;t<SIZE_BOARD;t++)
        result[t]=board[linia][t];
    return result;
}

int busca_marca(char linia_board[SIZE_BOARD], int inici, int final)
{
    
    if (inici > 0)
        inici--;
    if (final < SIZE_BOARD - 1)
        final++;
    int veins = 0;
    for (int t = inici; t <= final; t++)
    {
        if (linia_board[t] != CODI && !isdigit(linia_board[t]))
            veins++;
    }
   // printf("linia %s [%d, %d] --> %d veins\n", linia_board,inici,final,veins);
    return veins;
}

int buscar_veins(char board[SIZE_BOARD][SIZE_BOARD], int linia, int inici, int final)
{
    int veins = 0;
    // linia d'adalt
    if (linia > 0)
        veins += busca_marca(copia_linia(board,linia - 1), inici, final);
    // linia del numeo
    veins += busca_marca(copia_linia(board,linia), inici, final);
    if (linia < SIZE_BOARD - 1)
        veins += busca_marca(copia_linia(board,linia + 1), inici, final);
    return veins;
}

void printa_taulell(char board[SIZE_BOARD][SIZE_BOARD])
{
    for (int t = 0; t < SIZE_BOARD; t++)
    {
        for (int i = 0; i < SIZE_BOARD; i++)
        {
            printf("%c", board[t][i]);
        }
        printf("\n");
    }
}

int main()
{

    FILE *fp;
    ssize_t read;

    char *linia = NULL;
    size_t len_read = 0;

    // taulell
    char board[SIZE_BOARD][SIZE_BOARD];

    // resultat
    int resultat = 0;

    // obrim el fitxer en mode lectura
    fp = fopen(FILENAME, "r");
    if (fp == NULL)
    {
        exit(EXIT_FAILURE); // constant definida a stdlib.h
    }
    // anem llegint linia el taulell
    int pos_linia = 0;
    while ((read = getline(&linia, &len_read, fp)) != -1)
    {
        for (int t = 0; t < SIZE_BOARD; t++)
        {
            board[pos_linia][t] = linia[t];
        }
        pos_linia++;
    }

    printa_taulell(board);

    // mirem linia a linia si hi ha un numero i tornem les posicions que ocupen
    for (int t = 0; t < SIZE_BOARD; t++)
    {

        int i = 0;
        while (i < SIZE_BOARD)
        {
            int current_num = 0;
            int ini_num = -1;
            int fin_num = -1;
            if (isdigit(board[t][i]))
            {
                while (isdigit(board[t][i]) && i < SIZE_BOARD)
                {
                    if (ini_num < 0)
                        ini_num = i;
                    fin_num = i;
                    current_num =current_num*10 +  numero(board[t][i]) ;
                    i++;
                }
            }
            else
            {
                i++;
            }
            if (current_num > 0)
            {
                int veins = buscar_veins(board, t, ini_num, fin_num);
                if (veins == 0)
                {
                    printf("num %d, no te veins\n", current_num);
                } else {
                    resultat += current_num;
                     printf("num %d, te %d veins\n", current_num, veins);
                }
            }
        }
    }
    printf("acumulat es %d", resultat);
    fclose(fp);
    if (linia)
        free(linia);
    exit(EXIT_SUCCESS);

    return 1;
}
