import React from 'react';
import classNames from 'classnames';
import { SectionTilesProps } from '../../utils/SectionProps';
import SectionHeader from './partials/SectionHeader';

const propTypes = {
  ...SectionTilesProps.types
}

const defaultProps = {
  ...SectionTilesProps.defaults
}

const GenerationSection = ({
  className,
  topOuterDivider,
  bottomOuterDivider,
  topDivider,
  bottomDivider,
  hasBgColor,
  invertColor,
  pushLeft,
  ...props
}) => {

  const outerClasses = classNames(
    'features-tiles section',
    topOuterDivider && 'has-top-divider',
    bottomOuterDivider && 'has-bottom-divider',
    hasBgColor && 'has-bg-color',
    invertColor && 'invert-color',
    className
  );

  const innerClasses = classNames(
    'features-tiles-inner section-inner pt-0',
    topDivider && 'has-top-divider',
    bottomDivider && 'has-bottom-divider'
  );

  const tilesClasses = classNames(
    'tiles-wrap center-content',
    pushLeft && 'push-left'
  );

  const sectionHeader = {
    title: ' ',
    paragraph: ''
  };

  return (
    <section
      {...props}
      className={outerClasses}
    >
      <div className="container">
        <div className={innerClasses}>
          <SectionHeader data={sectionHeader} className="center-content" />
          <div className={tilesClasses}>
            <div className="form">
              <input type="text" id="prompt" className="form__input" autoCorrect="off" placeholder=" "/>
              <label for="prompt" className="form__label">Prompt</label>
            </div>
            <div className="button-ctr" onClick={get_generated_set_from_prompt}>Generate</div>
            <div className="grid-ctr">
              <div className="basic-grid" id="generated-vocab">
              </div>
            </div>
            <label className='grid-ctr-label' id="generated-label">Generated Vocabulary</label>
          </div>
        </div>
      </div>
    </section>
  );
}

GenerationSection.propTypes = propTypes;
GenerationSection.defaultProps = defaultProps;

function add_to_global_window (pair) {
  let list = document.getElementById("global-vocab");

  let newDiv = document.createElement("div");
  let rDiv = document.createElement("div");
  let lDiv = document.createElement("div");
  rDiv.setAttribute("id", 'trn');
  lDiv.setAttribute("id", 'src');
  rDiv.innerHTML = pair[0];
  lDiv.innerHTML = pair[1];

  newDiv.appendChild(lDiv);
  newDiv.appendChild(rDiv);

  list.appendChild(newDiv);
}

function add_to_generation_window (pair) {
  let list = document.getElementById("generated-vocab");

  let newDiv = document.createElement("div");
  let rDiv = document.createElement("div");
  let lDiv = document.createElement("div");
  rDiv.setAttribute("id", 'trn');
  lDiv.setAttribute("id", 'src');
  rDiv.innerHTML = pair[0];
  lDiv.innerHTML = pair[1];

  newDiv.appendChild(lDiv);
  newDiv.appendChild(rDiv);

  newDiv.addEventListener('click', function () {
    add_to_global_window(pair);
  });

  list.appendChild(newDiv);
}

function add_demo_stuff() {
  add_to_generation_window(["I'm feeling ...", "Me siento ..."]);
  add_to_generation_window(["energized", "lleno de energía"]);
  add_to_generation_window(["alert", "alerta"]);
  add_to_generation_window(["focused", "concentrado"]);
  add_to_generation_window(["after drinking coffee", "despues de beber café"]);
  add_to_generation_window(["I am in love with coffee", "Estoy enamorada del café"]);
  add_to_generation_window(["Coffee", "Café"]);
}

async function get_generated_set_from_prompt () {
  const data = [
    {'cmd': document.getElementById("prompt").value.toString()}
  ];

  console.log("DATA TO BE SENT: ", data);

  await fetch("/demo", {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(data)
  }).then((res) => res.json()).then( (res2) => {
    var obj = JSON.parse(JSON.stringify(res2));
    for (let i = 0; i < Object.keys(obj).length; i++) {
      add_to_generation_window([res2[i]['SRC'], res2[i]['TRN']]);
    }
  }
  );

}
/*
document.addEventListener('keypress', async function (event) {
  var name = event.key;

  if (name === 'Enter') {
    console.log("submitted");
    const newEl = document.createElement("div");
    newEl.setAttribute("class", "card");

    const data = {
      'cmd': document.getElementById("prompt").value.toString()
    };

    let rawResponse = await fetch(prodURL, {
      method: 'POST',
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json"
      },
      body: JSON.stringify(data)
    });

    newEl.innerHTML = document.getElementById("prompt").value;
    document.getElementById("generated-vocab").appendChild(newEl);
    document.getElementById("prompt").value = '';
  }
})*/

export default GenerationSection;