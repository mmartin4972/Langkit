import React, { useState } from 'react';

import './scss/styles.js';

import TopicView from './components/TopicView';
import CommandWindow from './components/CommandWindow';
import GenerationWindow from './components/GenerationWindow';
import TopicList from './components/TopicList';

// something to get a list of the names of all of the topics in the user's account

async function getUserTopics(userName) {
  const request_data = [
    {'request-type': 'user-topics'},
    {'username': userName}
  ];

  const the_list = [];

  await fetch("/data", {
    method: 'GET',
    headers: {
      "Content-Type": "application/json",
      "Accept": "application/json"
    },
    body: JSON.stringify(request_data)
  }).then((res) => res.json()).then( (res2) => {
    var obj = JSON.parse(JSON.stringify(res2));
    for (let i = 0; i < Object.keys(obj).length; i++) {
      the_list.push(res2[i]['name']);
    }
  }
  );

  return the_list;
}


const defaultTopic = [
  {'id': 0, 'source': 'banana', 'translation': 'platana'},
  {'id': 1, 'source': 'banana', 'translation': 'platana'},
  {'id': 2, 'source': 'banana', 'translation': 'platana'},
  {'id': 3, 'source': 'banana', 'translation': 'platana'},
  {'id': 4, 'source': 'banana', 'translation': 'platana'},
  {'id': 5, 'source': 'banana', 'translation': 'platana'},
  {'id': 6, 'source': 'banana', 'translation': 'platana'},
  {'id': 7, 'source': 'banana', 'translation': 'platana'}
]



class App extends React.Component {
  constructor (props) {
    super(props)
    this.state = {
      user: 'Carson',
      conversationHistory: [{'lk': 'Ask Me Anything...'}],
      currentTopic: defaultTopic
    };
  }

  deleteTopic (topicId) {
    const newList = this.state.topics.filter(a => a.id !== topicId);
    console.log(newList);
    this.setState({topics: newList})
  }

  deletePair (pairId) {
    const newList = this.state.currentTopic.filter(a => a.id !== pairId);
    this.setState({currentTopic: newList})
  }

  setCurrentTopic() {

  }


  render () {
    return (
        <div className='app-view-container'>
          <button id='anki-export'></button>
          <button id='save'></button>
          <button id='add-topic'></button>
          <TopicList userName={this.state.user}></TopicList>
          <TopicView></TopicView>
          <GenerationWindow></GenerationWindow>

        </div>
    );
  }
}

export default App;
