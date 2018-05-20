#include <stdio.h>
#include <stdlib.h> 

int main() {
  printf("Ожидание имени файла...\n");
  char nameFile[200];
  scanf("%s", nameFile);

  FILE *fileInput = fopen(nameFile, "rt");

  char *fwname = "./ip71_machehin_01_output.txt ";
  FILE *fileOutput = fopen(fwname, "w");;

  int count;
  fscanf(fileInput, "%i", &count);

  int arr[count];
  int key;
  for (key = 0; key < count; key++) {
    fscanf(fileInput, "%i", &arr[key]);
  }
  fclose(fileInput);

  for (key = 0; key < count; key++) {
    if (arr[key]%2 == 1) {
      continue;
    } else {
      int inkey = key;
      for (; inkey > 0; inkey--) {
        if (arr[inkey - 1]%2 == 1 | arr[inkey] <= arr[inkey - 1]) {
          int temp = arr[inkey];
          arr[inkey]  = arr[inkey - 1];
          arr[inkey - 1] = temp;
        }
      }
    }
  }

  for (key = count - 2 ; arr[key] % 2 == 1; key--) {
    int inkey = key;
    for ( ; inkey < count - 1; inkey++) {
      if (arr[inkey] < arr[inkey + 1]) {
        int temp = arr[inkey];
        arr[inkey] = arr[inkey + 1];
        arr[inkey + 1] = temp;
      }
    }
  }
  
  for (key = 0; key < count; key++){
    fprintf(fileOutput, "%i\n", arr[key]);
  }
  fclose(fileOutput);
  return 0;
}