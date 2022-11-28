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
                                <div>
                                    <div id='src'>{pair.source}</div>
                                    <div id='mid'></div>
                                    <div id='trn'>{pair.translation}</div>
                                </div>
                            );
                        })
                    }
                </div>
            </div>
        </>
    );
}


export default GenerationWindow;