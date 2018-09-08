'use strict';

const autors = [
  'Agatha Christie',
  'William Shakespeare',
  'Barbara Cartland',
  'Danielle Steel',
  'Harold Robbins',
  'Georges Simenon',
  'Sidney Sheldon',
  'Enid Blyton',
  'J. K. Rowling',
  'Dr. Seuss',
  'Gilbert Patten',
  'Eiichiro Oda',
  'Leo Tolstoy',
  'Corín Tellado'
];

const n = autors.length;

for (let k = parseInt(n / 2); k > 0; k = parseInt(k / 2)) {
  for (let i = k; i < n; i++) {
    for (let j = i; j >= k; j -= k) {
      if (autors[i] < autors[j - k]) {
        const temp = autors[j - k];
        autors[j - k] = autors[i];
        autors[i] = temp;
      } else break;
    }
  }
}

console.log(autors);

const autors2 = [
  'Agatha Christie',
  'William Shakespeare',
  'Barbara Cartland',
  'Danielle Steel',
  'Harold Robbins',
  'Georges Simenon',
  'Sidney Sheldon',
  'Enid Blyton',
  'J. K. Rowling',
  'Dr. Seuss',
  'Gilbert Patten',
  'Eiichiro Oda',
  'Leo Tolstoy',
  'Corín Tellado'
];

for (const i in autors2) {
  for (let j = i - 1; j >= 0; j--) {
    if (autors2[[j] > autors2[j + 1]]) {
      const temp = autors[j - 1];
      autors[j - 1] = autors[j];
      autors[j] = temp;
    }
  }
}
