#include <stdio.h>
#include <time.h>
#include <stdlib.h>

using namespace std;

int main() {
    int min = 1;
    int max = 10;

    srand(time(NULL));
    int rand_number = rand() % (max - min + 1) + min;

    printf("Find the number between %d and %d\n", min, max);

    int nb_found = -1;

    while (nb_found != rand_number) {
        printf("Your proposition ? ");
        scanf("%d", &nb_found);
        
        if (nb_found > rand_number) {
            printf("Too much high.\n");
        } else if (nb_found < rand_number) {
            printf("Too much low.\n");
        } else {
            printf("Exactly.\n");
            break;
        }
    }
}