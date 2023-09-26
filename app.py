from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



items = []
next_id = 1


@app.route('/')
def listar_itens():
    return render_template('listar_itens.html', items=items)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar_item():
    global next_id
    if request.method == 'POST':
        nome = request.form['nome']
        item = {'id': next_id, 'nome': nome}
        next_id += 1
        items.append(item)
        return redirect(url_for('listar_itens'))
    else:
        return render_template('adicionar_item.html')


@app.route('/editar/<int:item_id>', methods=['GET', 'POST'])
def editar_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return "Item não encontrado", 404

    if request.method == 'POST':
        item['nome'] = request.form['nome']
        return redirect(url_for('listar_itens'))
    return render_template('editar_item.html', item=item)


@app.route('/excluir/<int:item_id>', methods=['POST'])
def excluir_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return redirect(url_for('listar_itens'))

if __name__ == '__main__':
    app.run(debug=True)