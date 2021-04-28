# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

APP SERVICE: The costs, scalability, and availability for a Article CMS app deployed through an App Service is simple and efficient.
             Article CMS is a fairly simple application, so there is no much compute power capability is required. So even though
the service plans are constant and the user is paying even when no one is accessing the service, the
reduced compute requirements of a CMS app are not expensive. Continous deployment through GitHub workflows
on the Azure portal makes updating the CMS app is simply super.

Virtual Machine: The costs, scalability, and availability for a CMS app deployed through a VM are reasonablly high.
                 Virtual Machines are usually better when you need control of the underlying operating system or are using
custom software to support your needs; an app service is typically better for lightweight applications and
services, especially when you don't have the need for high performance compute services.
Additionally, need to take into consideration the hardware limitations of App Services.

My Preference: For Article CMS project compute option App Service is the best. In a simple terms Article CMS app is lightweight,
           does not require robust compute power. The CMS App is deployed in a simple and straightforward manner and
  runs on a Python codebase, which is supported by App Service.
  
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

APP Service: Once Article CMS application started gaining popularity then it would demand more compute resources.
             If we add any features then cost factor also increases. Its a kind of dependency on cloud provider which means
if cloud provider doesn't support application features and then definately it will impact loosing customers.

VM: Once Article CMS application started gaining popularity then it could become more expensive due to significant compute power.
    Any new onboarding needs to know customization process of VM, so the on-boarding for new developers and operations team
would take sufficient time. If the CMS demands more compute capability, then cost factor also increases.


Each of these has their own use cases, although sometimes there is still some ambiguity on when to use each. 
