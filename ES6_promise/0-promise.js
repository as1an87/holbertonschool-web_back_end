// 0-promise.js
export default function getResponseFromAPI() {
  return new Promise((resolve, reject) => {

    setTimeout(() => {
      const success = true;

      if (success) {
        resolve('Başarı');
      } else {
        reject('Hata');
      }
    }, 1000);
  });
}
