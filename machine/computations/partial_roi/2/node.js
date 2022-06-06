import fetch from "node-fetch";

const response = await fetch(
  "https://netent-game.casinomodule.com/servlet/CasinoGameServlet;jsession=DEMO-1428084744-EUR?action=spin&sessid=DEMO-1428084744-EUR&gameId=victorious_not_mobile&wantsreels=true&wantsfreerounds=true&freeroundmode=false&bet.betlevel=10&bet.denomination=50&bet.betlines=243&bet.mathMode=classic&no-cache=ae781099-f05f-438f-a235-7cfab3c16075&bettingmode=coins",
  {
    headers: {
      accept: "*/*",
      "accept-language": "es-AR,es;q=0.9,en-US;q=0.8,en;q=0.7,es-419;q=0.6",
      "sec-ch-ua":
        '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
      "sec-ch-ua-mobile": "?0",
      "sec-ch-ua-platform": '"Windows"',
      "sec-fetch-dest": "empty",
      "sec-fetch-mode": "cors",
      "sec-fetch-site": "same-site",
      Referer: "https://netent-static.casinomodule.com/",
      "Referrer-Policy": "strict-origin-when-cross-origin",
    },
    body: null,
    method: "GET",
  }
);

const data = await response.text();
const x = data.indexOf("pos");
const post = [];

const sourceStr = data;
const searchStr = "pos=";
const indices = [...sourceStr.matchAll(new RegExp(searchStr, "gi"))].map(
  (a) => a.index
);

console.log(indices);

for (let index = 0; index < indices.length; index++) {
  const element = indices[index];
  console.log(data.slice(element, element + 7));
}

// indices.map((ind) => {
//   data.slice(ind, ind + 5);
// });

// console.log(indices);

// console.log(x);

// console.log("data", data, typeof data);
