import '../styles/styles'

function GenerationWindow (props) {

    const tempList = [
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Word One', 'translation': 'Word One'},
        {'source': 'Togepi is in front of me and looks nice', 'translation': 'Togepi es en el frente de yo, y mira bueno'}
    ]

    return (
        <>
            <div className="grid-ctr">
                <div className="basic-grid" id="generated-vocab">
                    {tempList.map(pair => {
                            return (
                                <button onClick={() => props.addPair(pair.source, pair.translation)}>
                                    <div id='src'>{pair.source}</div>
                                    <div id='mid'></div>
                                    <div id='trn'>{pair.translation}</div>
                                </button>
                            );
                        })
                    }
                </div>
            </div>
        </>
    );
}


export default GenerationWindow;