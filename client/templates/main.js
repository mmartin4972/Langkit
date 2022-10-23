function mic_click () {
  console.log("Clicked the Mic button");

  eel.mic_click()(mic_click_callback);
}

function mic_click_callback (str) {
  document.getElementById("response-window-text-box").value = str;

  generate_phrases_from_text(str);
}

function add_to_global_list (pair) {
  let globalList = document.getElementById("global-vocab-list");

  let newChild = document.createElement("li");

  newChild.setAttribute("class", "vocab-pair");

  let sourceDiv = document.createElement("div");
  let transDiv = document.createElement("div");
  sourceDiv.setAttribute("class", "source-text-box");
  transDiv.setAttribute("class", "trans-text-box");
  sourceDiv.innerHTML = pair[0]
  transDiv.innerHTML = pair[1]

  newChild.appendChild(sourceDiv);
  newChild.appendChild(transDiv);

  globalList.appendChild(newChild);
}

async function get_translated_list (list) {
  return eel.quick_translate_list(list)();
}

async function generate_phrases_from_text (str) {
  const words = str.split(' ');
  let translations = await get_translated_list(words);

  let generatedList = document.getElementById("generated-vocab-list");

  while (generatedList.firstChild) {
    generatedList.removeChild(generatedList.firstChild);
  }

  for (let i = 0; i < words.length; i++) {
    let newChild = document.createElement("li");

    newChild.setAttribute("class", "vocab-pair");

    let pair = [words[i], translations[i]];

    newChild.addEventListener('click', function () {
      add_to_global_list(pair)
    });

    let sourceDiv = document.createElement("div");
    let transDiv = document.createElement("div");
    sourceDiv.setAttribute("class", "source-text-box");
    transDiv.setAttribute("class", "trans-text-box");
    sourceDiv.innerHTML = words[i]
    transDiv.innerHTML = translations[i];

    newChild.appendChild(sourceDiv);
    newChild.appendChild(transDiv);

    generatedList.appendChild(newChild);
  }
}