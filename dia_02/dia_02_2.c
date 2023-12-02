#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//#define FILENAME "sample.txt"
// #define FILENAME "sample2.txt"
#define FILENAME "input.txt"

#define POSICIO_ID 5
#define MAX_RED 12
#define MAX_BLUE 14
#define MAX_GREEN 13

int numeroDeDigits(int numero)
{
    return (int)((ceil(log10(numero)) + 1) * sizeof(char));
}

int numero(char c)
{
    return (int)c - 48;
}

int tornaID(char *linia)
{
    // mirem el ID, depened de la posicio del : sabrem si te 1, 2 o 3 digits
    if (linia[POSICIO_ID + 3] == ':')
        return numero(linia[POSICIO_ID]) * 100 + numero(linia[POSICIO_ID + 1]) * 10 + numero(linia[POSICIO_ID + 2]);
    else if (linia[POSICIO_ID + 2] == ':')
        return numero(linia[POSICIO_ID]) * 10 + numero(linia[POSICIO_ID + 1]);
    else if (linia[POSICIO_ID + 1] == ':')
        return numero(linia[POSICIO_ID]);
    else
        return -1;
}

int main()
{

    FILE *fp;
    ssize_t read;

    char *linia = NULL;

    // tamany de la linia
    size_t len_read = 0;
    int len = 0;

    int resultat = 0;

   int red = 0;
        int blue = 0;
        int green = 0;

       int max_red = 0;
        int max_blue = 0;
        int max_green = 0;


    // obrim el fitxer en mode lectura
    fp = fopen(FILENAME, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE); // constant definida a stdlib.h

    // anem llegint linia a linia fis que getline torna un -1
    while ((read = getline(&linia, &len_read, fp)) != -1)
    {
        red = 0;
        blue = 0;
        green = 0;
        max_red = 0;
        max_blue = 0;
        max_green = 0;


        printf("-------------------------------------------\n");
        printf("linia %s\n", linia);
        int id = 0;
     
     
        int numero_boles = 0;

        // agadem el tamany real de la linia
        len = strlen(linia);
        id = tornaID(linia);
        printf("id %d\n", id);
        // loop per buscar els numeros i els colors, ens situem a la primera poscio, depen del numero de digits del ID
        int posicio = POSICIO_ID + 2;
        if (id < 10)
            posicio += 1;
        else if (id < 100)
            posicio += 2;
        else
            posicio += 3;

        while (posicio < len)
        {
            // printf("posicion %d\n", posicio);
            // printf("caracter llegit %c\n", linia[posicio]);
            // mirem si estem al comenáment de una bola
            if (isdigit(linia[posicio]))
            {
                // mirem si el numero de 1 o 2 digits
                if (isdigit(linia[posicio + 1]))
                {
                    numero_boles = numero(linia[posicio]) * 10 + numero(linia[posicio + 1]);
                    // ens situem al comenáment del tipus de bola
                    posicio = posicio + 3;
                }
                else
                {
                    numero_boles = numero(linia[posicio]);
                    // ens situem al comenáment del tipus de bola
                    posicio = posicio + 2;
                }
                // printf("numero de boles %d\n", numero_boles);
                // mirem quina bola es, podriem avançar posicio i salta al seguent pero no val la pena, ja es prou rapid
                if (len - posicio >= strlen("red") && linia[posicio] == 'r' && linia[posicio + 1] == 'e' && linia[posicio + 2] == 'd')
                    red = red + numero_boles;
                else if (len - posicio >= strlen("blue") && linia[posicio] == 'b' && linia[posicio + 1] == 'l' && linia[posicio + 2] == 'u' && linia[posicio + 3] == 'e')
                    blue = blue + numero_boles;
                else if (len - posicio >= strlen("green") && linia[posicio] == 'g' && linia[posicio + 1] == 'r' && linia[posicio + 2] == 'e' && linia[posicio + 3] == 'e' && linia[posicio + 4] == 'n')
                    green = green + numero_boles;
            }
            //mire que passa quan acabaem una tirada
            else if (linia[posicio] == ';')
            {
                //si el numero de boles necessaries es > que el que tenim fins ara actualitzem
                if (max_red < red)
                    max_red = red;
                if (max_green < green)
                    max_green = green;
                if (max_blue < blue)
                    max_blue = blue;
                //posem a zero les boles i avancem una posicio al string per mirar el seguent carated    
                red = 0;
                blue = 0;
                green = 0;
                posicio++;
            }
            else
            {
                // si no es numero llegim el seguent caracter
                posicio++;
            }
        }
        //tractem la ultima tirada, no acana en ; per tant no l'hem tractat abans
        if (max_red < red)
            max_red = red;
        if (max_green < green)
            max_green = green;
        if (max_blue < blue)
            max_blue = blue;

        printf("red=%d blue=%d green=%d\n", max_red, max_blue, max_green);
        resultat+=max_blue*max_green*max_red;    
    }
    printf("acumulat es %d", resultat);
    fclose(fp);
    if (linia)
        free(linia);
    exit(EXIT_SUCCESS);
}