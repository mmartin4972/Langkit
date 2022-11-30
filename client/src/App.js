import './styles/styles'
import TopicListView from './components/TopicListView';
import TopicView from './components/TopicView';
import CommandWindow from './components/CommandWindow';
import GenerationWindow from './components/GenerationWindow';

import { Component } from 'react';


async function testFetch (sourceLang, targetLang) {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
    body: JSON.stringify([{ 
      cmd: 'Generate me phrases about a dinner party' ,
      sourceLang: sourceLang,
      targetLang: targetLang
    }])
  };

  fetch('/parse-cmd', requestOptions)
    .then(response => {console.log(response); return response.json();})
    .then(res => {
      console.log(res);
      /*
      let a = Array.from(res);
      for (let i = 0; i < a.length; i++) {
        console.log(a[i]);
      }*/
    })
    .catch(error => console.log(error));
}


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      topics: [
        {
          id: 0,
          name: 'Create New Topic',
          sourceLang: 'NONE',
          targetLang: 'NONE',
          list: []
        },
        {
          id: 1,
          name: 'Fruit',
          sourceLang: 'ES',
          targetLang: 'EN',
          list: [
            {
              id: 0,
              source: 'Manzana',
              translation: 'Apple'
            },
            {
              id: 1,
              source: 'Naranja',
              translation: 'Orange'
            },
            {
              id: 2,
              source: 'Platana',
              translation: 'Banana'
            }
          ]
        },
        {
          id: 2,
          name: 'Fruit but Blue',
          sourceLang: 'ES',
          targetLang: 'EN',
          list: [
            {
              id: 0,
              source: 'Manzana pero azul',
              translation: 'Apple but blue'
            },
            {
              id: 1,
              source: 'Naranja pero azul',
              translation: 'Orange but blue'
            },
            {
              id: 2,
              source: 'Platana pero azul',
              translation: 'Banana but blue'
            }
          ]
        },
        {
          id: 3,
          name: 'Fruit but bluer',
          sourceLang: 'ES',
          targetLang: 'EN',
          list: [
            {
              id: 0,
              source: 'Manzana pero azul',
              translation: 'Apple pero azul'
            },
            {
              id: 1,
              source: 'Naranja pero azul',
              translation: 'Orange pero azul'
            },
            {
              id: 2,
              source: 'Platana pero azul',
              translation: 'Banana pero azul'
            }
          ]
        }
      ],
      cmd_window_pairs: [
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frentTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoe de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el Togepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenoTogepi es en el frente de yo, y mira buenofrente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'}
      ],
      selectedTopic: 1
    };
  }

  setSelectedTopic = (newTopicId) => {
    this.setState({selectedTopic: newTopicId});
  }

  createNewTopic = () => {
    const newList = [...this.state.topics];
    const currentSrc = document.getElementById('source-selector').innerHTML;
    const currentTrgt = document.getElementById('target-selector').innerHTML;

    newList.push({
      id: 0,
      name: 'Untitled Topic',
      sourceLang: currentSrc,
      targetLang: currentTrgt,
      list: []
    });

    let count = 0;
    for (let i = 0; i < newList.length; i++) {
      newList[i].id = i;
      count = i;
    }

    this.setState({topics: newList});
    this.setState({selectedTopic: count});
  }

  deleteTopic = (topicId) => {
    var newList = [...this.state.topics]

    newList.splice(topicId, 1);

    this.setState({topics: newList});
    this.setState({selectedTopic: 0});
  }

  addPair = (source, translation) => {
    const newList = [...this.state.topics];
    var newSubList = newList[this.state.selectedTopic].list;

    newSubList.push({
      id: 0,
      source: source,
      translation: translation
    });

    for (let i = 0; i < newSubList.length; i++) {
      newSubList[i].id = i;
    }
    


    this.setState({topics: newList});
  }

  deletePair = (pairId) => {
    var newList = [...this.state.topics];
    var newSubList = newList[this.state.selectedTopic].list;

    var copy = [...newSubList];
    console.log(copy, "Splicing ", pairId);
    newSubList.splice(pairId, 1);
    copy = [...newSubList];
    console.log(copy);

    for (let i = 0; i < newSubList.length; i++) {
      newSubList[i].id = i;
    }

    newList[this.state.selectedTopic].list = newSubList;

    this.setState({topics: newList});
  }

  changeTopicNameBoxValue = () => {
    const text = document.getElementById('topic-name-edit-box').value;

    const list = [...this.state.topics]

    list[this.state.selectedTopic].name = text;

    this.setState({topics: list});
  }

  render() {
    console.log(this.state.topics);
    return (
      <div className='app-view-container'>
        <button id='anki-export' onClick={testFetch}></button>
        <TopicListView 
          topics={this.state.topics} 
          setSelectedTopic={this.setSelectedTopic.bind(this)} 
          selectedTopic={this.state.selectedTopic} 
          deleteTopic={this.deleteTopic.bind(this)}
          createNewTopic={this.createNewTopic.bind(this)}/>
        <TopicView 
          pairs={this.state.topics[this.state.selectedTopic].list} 
          deletePair={this.deletePair.bind(this)} 
          selectedTopicId={this.state.selectedTopic}
          selectedTopicName={this.state.topics[this.state.selectedTopic].name}
          changeTopicNameBoxValue={this.changeTopicNameBoxValue.bind(this)}/>
        <CommandWindow />
        <GenerationWindow 
          pairs={this.state.cmd_window_pairs} 
          addPair={this.addPair.bind(this)}/>
      </div>
    );
  }
}

export default App;
