import './styles/styles'

import TopicListView from './components/TopicListView';
import TopicView from './components/TopicView';
import GenerationView from './components/GenerationView';


function App() {
  return (
    <div className='app-view-container'>
      <button id='anki-export'></button>
      <button id='save'></button>
      <button id='add-topic'></button>
      <TopicListView />
      <TopicView />
      <GenerationView />
    </div>
  );
}

export default App;
