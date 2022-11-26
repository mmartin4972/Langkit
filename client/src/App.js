import './styles/styles'
import TopicListView from './components/TopicListView';
import TopicView from './components/TopicView';
import GenerationView from './components/GenerationView';


async function testFetch () {
  
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Accept':'application/json' },
    body: JSON.stringify({ cmd: 'Generate me phrases about a dinner party' })
  };
  fetch('/parse-cmd', requestOptions)
    .then(response => {console.log(response); return response.json();})
    .then(res => console.log(res))
    .catch(error => console.log(error));
}

function App() {
  return (
    <div className='app-view-container'>
      <button id='anki-export'></button>
      <button id='save' onClick={testFetch}></button>
      <button id='add-topic'></button>
      <TopicListView />
      <TopicView />
      <GenerationView />
    </div>
  );
}

export default App;
