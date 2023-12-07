#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define FILENAME "sample.txt"
// #define FILENAME "sample2.txt"
// #define FILENAME "input.txt"

#define SIZE_BOARD 10
//#define SIZE_BOARD 140

#define CODI '.'

#define GEAR '*'

int torna_numero(char c)
{
    return (int)c - 48;
}

char *copia_linia(char board[SIZE_BOARD][SIZE_BOARD], int linia)
{
    char *result = calloc(SIZE_BOARD, sizeof(char));
    for (int t = 0; t < SIZE_BOARD; t++)
        result[t] = board[linia][t];
    return result;
}

int torna_veins_fila(char linia[SIZE_BOARD], int columna, int **resultat)
{

    int ini = -1;
    int fin = -1;
    int numero = 0;
    int pos_vei = 0;

  
    printf("torna veins de %s\n", linia);
    // anem buscant numeros
    for (int t = 0; t < SIZE_BOARD; t++)
    {
        if (isdigit(linia[t]))
        {
            if (ini < 0)
                ini = t;
            fin = t;
            numero = numero * 10 + torna_numero(linia[t]);
            //printf("digit %c tronat ini=%d, fin=%d  numero = %d\n", linia[t],ini,fin,numero);
        }
        else
        {
           // printf("No digit %c tronat ini=%d, fin=%d  numero = %d\n", linia[t],ini,fin,numero);
            if (ini >= 0)
            {
                // hi ha final de numero
                printf("Guardem ini=%d fin=%d col=%d\n",ini,fin,columna);
                if (columna >= (ini-1) && columna <= (fin+1))
                {
                    printf("Si, Guardem\n");
                    resultat[pos_vei++] = numero;
                   
                }
            }
            ini = -1;
            fin = -1;
            numero = 0;
        }
    }
    return pos_vei;
}

void printa_veins(int *veins, int len) {
    for(int t=0;t<len;t++) {
        printf("%d,",*veins);
    }
    printf("\n");
}

int buscar_veins(char board[SIZE_BOARD][SIZE_BOARD], int fila, int columna)
{
    int *veins = calloc(3, sizeof(int));
    int num_veins = 0;
    int num_veins_total = 0;
    int resultat = 1;
  
    if (fila > 0)
    {
        printf("busca fila anterior\n");
        num_veins = torna_veins_fila(copia_linia(board, fila - 1), columna, &veins);      
        printa_veins(veins,num_veins);
        printf("veins de fila=%d num_vv=%lu\n ",fila-1, sizeof(veins) / (sizeof(int)));
        num_veins_total = num_veins;
        for (int t = 0; t < num_veins; t++)
        {
            resultat *= veins[t];
        }
    }
    printf("busca fila \n");
    num_veins = torna_veins_fila(copia_linia(board, fila), columna,&veins);
    for (int t = 0; t < num_veins; t++)
    {
        resultat *= veins[t];
    }
    num_veins_total += num_veins;
    printf("veins de fila=%d num_vv=%lu\n ",fila, sizeof(veins) / (sizeof(int)));
  
    if (fila < SIZE_BOARD - 1)
    {
        printf("busca fila posterior\n");
        num_veins = torna_veins_fila(copia_linia(board, fila + 1), columna,&veins);
        num_veins_total = num_veins;
        for (int t = 0; t < num_veins; t++)
        {
            resultat *= veins[t];
        }
    }
    printf("veins de fila=%d num_vv=%lu\n ",fila+1, sizeof(veins) / (sizeof(int)));
    if (num_veins_total == 2)
        return resultat;
    else
        return -1;
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

    // mirem linia a linia si hi ha un asterisc
    for (int t = 0; t < SIZE_BOARD; t++)
    {
        for (int i = 0; i < SIZE_BOARD; i++)
        {
            if (board[t][i] == GEAR)
            {
                printf("busca veins de %d,%d\n", t, i);
                int veins = buscar_veins(board, t, i); // torna el producte si hi ha exactament 2 veins, si no -1
                if (veins > 0)                         // hi ha nomes
                    resultat += veins;
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
