from graphviz import Digraph

dot = Digraph(comment='AI Development Workflow')
dot.node('A', 'Problem Definition')
dot.node('B', 'Data Collection')
dot.node('C', 'Preprocessing')
dot.node('D', 'Feature Engineering')
dot.node('E', 'Model Training')
dot.node('F', 'Evaluation')
dot.node('G', 'Deployment')

dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG'])
dot.render('workflow_diagram', format='png', cleanup=True)
