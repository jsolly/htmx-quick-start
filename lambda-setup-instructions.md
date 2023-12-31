### Configuring the Lambda
1. Create a new lambda with the following settings:
* Function name - Htmx-Todo-lambda
* Runtime - Python 3.11
* Architecture - x86_64

Hit 'Create function'

2. The Lambda code window should open, replace the code with the following:
```py
def lambda_handler(event, context):
    return {
        'headers': {'content-type': 'text/html'},
        'statusCode': 200,
        'body': f'''
           <li><input type="checkbox" id="todo4"><label for="todo4">New Todo Via AWS Lambda!</label></li>
          '''
        }
```
3. Click the ‘Deploy’ button
4. Under the `Configuration` tab select `Function URL` from the left navigation panel
5. Then click the `Create function URL` button
6. Create a Function URL with the following properties:
* Auth type - `NONE`
7. Click 'Additional settings'
* Check the checkbox, `Configure cross-origin resource sharing (CORS)`
* Allow origin - `*` (allow all)
* Add the following values under “Expose headers”
  - access-control-allow-origin
  - access-control-allow-methods
  - access-control-allow-headers
* Add the following values under “Allow headers”
  - hx-current-url
  - hx-request
* Select the following values under “Allow methods”
  - GET
7. Click “Save"
8. Look for the `Function URL` (scroll down a little) and open it in a new tab, you should see:
```
New Todo Via AWS Lambda!
```