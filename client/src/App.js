import './styles/styles'
import TopicListView from './components/TopicListView';
import TopicView from './components/TopicView';
import CommandWindow from './components/CommandWindow';
import GenerationWindow from './components/GenerationWindow';

import { Component } from 'react';


async function testFetch () {
  
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
    body: JSON.stringify({ username: 'Carson' })
  };

  fetch('/parse-cmd', requestOptions)
    .then(response => {console.log(response); return response.json();})
    .then(res => {
      console.log(Array.from(res));
      let a = Array.from(res);
      for (let i = 0; i < a.length; i++) {
        console.log(a[i]);
      }
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
          id: 1,
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
          id: 2,
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
              id: 3,
              source: 'Platana pero azul',
              translation: 'Banana pero azul'
            }
          ]
        }
      ],
      selectedTopic: 0
    };
  }

  setSelectedTopic = (newTopicId) => {
    console.log("The button was clicked")
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

    for (let i = 0; i < newList.length; i++) {
      newList[i].id = i;
    }

    this.setState({topics: newList});
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
    const newList = [...this.state.topics];
    var newSubList = newList[this.state.selectedTopic].list;

    newSubList.splice(pairId, 1);

    for (let i = 0; i < newSubList.length; i++) {
      newSubList[i].id = i;
    }

    newList[this.state.selectedTopic].list = newSubList;

    this.setState({topics: newList});
  }

  render() {
    return (
      <div className='app-view-container'>
        <button id='anki-export'></button>
        <button id='save' onClick={testFetch}></button>
        <button id='add-topic' onClick={this.createNewTopic.bind(this)}></button>
        <TopicListView topics={this.state.topics} setSelectedTopic={this.setSelectedTopic.bind(this)}/>
        <TopicView pairs={this.state.topics[this.state.selectedTopic].list} deletePair={this.deletePair.bind(this)} selectedTopicId={this.state.selectedTopic}/>
        <CommandWindow />
        <GenerationWindow addPair={this.addPair.bind(this)}/>
      </div>
    );
  }
}

export default App;
